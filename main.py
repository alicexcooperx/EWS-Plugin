import parser_module
import sanitize_module
import redaction_module
import os


def main():
    """
    This is the main method which is used as a wrapper class for the program.

    It is also used to store main part of the redaction code.
    The code, takes in the values of the BE output and splits the file by redact_file, redact_location and
    redact_string. The redact file is the stored in a dictionary and counts up the bytes which belong to redact_string.
    The bytes counted are then replaced by *, each file has a .redacted file outputted with the original file.

    | @param: None
    """
    ticket = open("ticket.json", "r")
    ticket_contents = ticket.read()
    ticket.close()

    parsing = parser_module.parser_module()
    dto_object = parsing.parse_ticket(ticket_contents)
    sanitise = sanitize_module.sanitize_module()
    sanitise.sanitise_av(dto_object)
    redaction_class = redaction_module.redaction_module()
    redaction = {}

    for file_n in os.listdir(redaction_class.full_directory_path):
        # For each file in the directory of the output open the files
        if file_n == "report.xml" or file_n == "json.txt":
            continue
        with open(os.path.join(os.getcwd(), file_n), 'r') as f:
            for line in f:
                # Gets values for file, location and the string to redact
                try:
                    redact_file = os.path.normpath(line.split('\t')[0].split('ô€€œ-')[0])
                    redact_location = line.split('\t')[0].split('ô€€œ-')[1]
                    redact_string = line.split('\t')[1]

                    # Creating temp so that we can cast the location into an integer.
                    temp_cast = int(redact_location)

                    for letter in redact_string:
                        # If the redact file isn't in redaction, it creates a list with the first object being
                        # temp_location and adds one byte for each letter.
                        if redact_file not in redaction:
                            temp = [temp_cast]
                            redaction[redact_file] = temp
                            temp_cast += 1
                            print(redact_file)
                        else:
                            # Else it appends it and adds one for each letter of the redact_file.
                            file_name_key = redaction.get(redact_file)
                            file_name_key.append(temp_cast)
                            temp_cast += 1

                except IndexError:
                    continue

    keys = redaction.keys()
    # Creates a dictionary called redaction
    for key in keys:
        # Get the value associated to that key, sort the bytes, cap the size so the memory isn't overwhelmed.
        bytes_to_redact = redaction.get(key)
        bytes_to_redact.sort()
        byte_count = 1024
        byte = 0
        in_file = open(key, "rb")
        out_file = open((key + ".redacted"), "wb")

        while True:
            # while the condition is true read the byte count into the buffer
            buffer = in_file.read(byte_count)

            if buffer == b"":
                # It returns if it is empty
                break

            if redaction_class.value_contains(bytes_to_redact, byte, byte_count):
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
