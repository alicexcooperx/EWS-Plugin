from datetime import datetime
import os
import glob


class Redaction:

    def redactionbulk(self):
        """
        Creates a directory of files which is based on the current date and time
        Runs Bulk_Extractor on the attachments file which is related to the DTO

        | @param self: access the attributes of the class
        """
        date_time_obj = datetime.now()
        time_string = date_time_obj.strftime("%d-%b-%Y %H-%M-%S")
        directory = time_string
        parent_dir = r"C:\\Users\\angel\\OneDrive\\Documents\\Diss\\"
        full_directory_path = parent_dir + directory
        command = 'bulk_extractor -o "' + full_directory_path + '" -R "C:\\Users\\angel\\PycharmProjects\\EWS-Plugin' \
                                                                '\\attachments" '
        os.system(command)

    def removefiles(self, fullDirectoryPath):
        """
        Removes all of the files which have 0KB in them so that the program can ignore irrelevant files.

        | @param self: access the attributes of the class
        | @param fullDirectoryPath: Passes the full directory path
        """
        in_dir = fullDirectoryPath
        os.chdir(in_dir)
        file_list = glob.glob("*.txt")

        for filename in file_list:
            if os.stat(filename).st_size == 0:
                os.remove(filename)

    def valueContains(self, redactArray, startPos, increment):
        """
        Removes all of the files which have 0KB in them so that the program can ignore irrelevant files.

        | @param self: access the attributes of the class
        | @param redactArray: The array of information that has been found that needs to be redacted
        | @param startPos: The start position of the byte of sensitive information
        | @param increment: The increment of the byte
        """
        test_result = startPos
        for x in range(increment):
            if test_result in redactArray:
                return True
            test_result += 1
        return False

    with open('attachmentsoutput\\domain.txt', 'r') as f:

        redaction = {}

        for line in f:
            try:
                redact_file = os.path.normpath(line.split('\t')[0].split('ô€€œ-')[0])
                redact_location = line.split('\t')[0].split('ô€€œ-')[1]
                redact_string = line.split('\t')[1]

                tempLocation = int(redact_location)

                for letter in redact_string:
                    fileNameKey = redaction.get(redact_file)
                    if not fileNameKey:
                        temp = [tempLocation]
                        redaction[redact_file] = temp
                        tempLocation += 1
                    else:
                        fileNameKey.append(tempLocation)
                        tempLocation += 1

            except IndexError:
                continue

        keys = redaction.keys()
        for key in keys:
            bytesToRedact = redaction.get(key)
            byteCount = 1024
            byte = 0
            inFile = open(key, "rb")
            outFile = open((key + ".redacted"), "wb")

            while True:
                buffer = inFile.read(byteCount)

                if buffer == b"":
                    break

                if valueContains(bytesToRedact, byte, byteCount):
                    for x in range(byteCount):
                        currentByte = byte + x

                        if currentByte in bytesToRedact:
                            outFile.write(b'*')
                        else:
                            outFile.write(buffer[x:(x+1)])

                else:
                    outFile.write(buffer)
                byte += byteCount
