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
    rdc = Redaction.Redaction()
    redaction = {}

    for filen in os.listdir(rdc.full_directory_path):
        if filen == "report.xml" or filen == "json.txt":
            continue
        with open(os.path.join(os.getcwd(), filen), 'r') as f:
            for line in f:
                # Gets values for file, location and the string to redact
                try:
                    redact_file = os.path.normpath(line.split('\t')[0].split('ô€€œ-')[0])
                    redact_location = line.split('\t')[0].split('ô€€œ-')[1]
                    redact_string = line.split('\t')[1]

                    tempLocation = int(redact_location)

                    # Gets the letter and make a temporary location if it doesnt exist.
                    for letter in redact_string:
                        if redact_file not in redaction:
                            temp = [tempLocation]
                            redaction[redact_file] = temp
                            tempLocation += 1
                        else:
                            fileNameKey = redaction.get(redact_file)
                            fileNameKey.append(tempLocation)
                            tempLocation += 1

                except IndexError:
                    continue

    keys = redaction.keys()
    for key in keys:
        # Want to make sure that the system isn't over-using memory so it has been limited.
        bytesToRedact = redaction.get(key)
        bytesToRedact.sort()
        byteCount = 1024
        byte = 0
        inFile = open(key, "rb")
        outFile = open((key + ".redacted"), "wb")

        while True:
            buffer = inFile.read(byteCount)

            if buffer == b"":
                break

            if rdc.valueContains(bytesToRedact, byte, byteCount):
                for x in range(byteCount):
                    currentByte = byte + x

                    if currentByte in bytesToRedact:
                        outFile.write(b'*')
                    else:
                        outFile.write(buffer[x:(x + 1)])

            else:
                outFile.write(buffer)
            byte += byteCount



if __name__ == '__main__':
    main()
