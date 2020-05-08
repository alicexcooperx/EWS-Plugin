from datetime import datetime
import os
import glob


class Redaction:

    def redactionbulk(self):

        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y %H-%M-%S")
        directory = timestampStr
        parent_dir = r"C:\\Users\\angel\\OneDrive\\Documents\\Diss\\"
        fullDirectoryPath = parent_dir + directory
        command = 'bulk_extractor -o "' + fullDirectoryPath + '" -R "C:\\Users\\angel\\OneDrive\\Documents\\Diss' \
                                                              '\\filesforBE" '
        os.system(command)

    def removefiles(self, fullDirectoryPath):
        inDir = fullDirectoryPath
        os.chdir(inDir)
        fileList = glob.glob("*.txt")

        for filename in fileList:
            if os.stat(filename).st_size == 0:
                os.remove(filename)

    def valueContains(redactArray, startPos, increment):
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












