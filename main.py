import Parser
import sanitizationVT
import Redaction
import os


def main():
    """
    This is the main method which is used as a wrapper class for the program.

    | @param: None
    """
    ticket = open("ticket.json", "r")
    ticket_contents = ticket.read()
    ticket.close()
    parsing = Parser.Parser()
    dto_object = parsing.parse_ticket(ticket_contents)
    sanitise = sanitizationVT.SanitizationAV()
    sanitise.sanitiseAV(dto_object)
    redaction_class = Redaction.Redaction()
    redaction = {}

    for filen in os.listdir(redaction_class.full_directory_path):
        # For each file in the directory of the output open the files
        if filen == "report.xml" or filen == "json.txt":
            continue
        with open(os.path.join(os.getcwd(), filen), 'r') as f:
            for line in f:
                # Gets values for file, location and the string to redact
                try:
                    redact_file = os.path.normpath(line.split('\t')[0].split('ô€€œ-')[0])
                    redact_location = line.split('\t')[0].split('ô€€œ-')[1]
                    redact_string = line.split('\t')[1]

                    temp_location = int(redact_location)

                    # Gets the each letter and make a temporary location if it doesnt exist.
                    for letter in redact_string:
                        if redact_file not in redaction:
                            temp = [temp_location]
                            redaction[redact_file] = temp
                            temp_location += 1
                        else:
                            file_name_key = redaction.get(redact_file)
                            file_name_key.append(temp_location)
                            temp_location += 1

                except IndexError:
                    continue

    keys = redaction.keys()
    for key in keys:
        # Want to make sure that the system isn't over-using memory so it has been limited.
        bytes_to_redact = redaction.get(key)
        # Sort from the smallest byte to the largest
        bytes_to_redact.sort()
        byte_count = 1024
        byte = 0
        # Read the in file and write to the out file in binary mode
        in_file = open(key, "rb")
        out_file = open((key + ".redacted"), "wb")

        while True:
            # while the condition is true read the byte count into the buffer
            buffer = in_file.read(byte_count)

            if buffer == b"":
                break

            if redaction_class.valueContains(bytes_to_redact, byte, byte_count):
                for x in range(byte_count):
                    current_byte = byte + x

                    if current_byte in bytes_to_redact:
                        out_file.write(b'*')
                    else:
                        out_file.write(buffer[x:(x + 1)])

            else:
                out_file.write(buffer)
            byte += byte_count


if __name__ == '__main__':
    main()
