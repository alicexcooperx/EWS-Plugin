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

    def redactionfind(self):
        piece_size = 4096
        out_file = open("C:\\Users\\angel\\OneDrive\\Documents\\DissRedactionBytes\\output.txt", "wb")
        in_file = open("C:\\Users\\angel\\OneDrive\\Documents\\DissRedactionBytes\\input.txt", "rb")

        while True:
            piece = in_file.read(piece_size)
            if piece == b"":
                break
            out_file.write(piece)
        out_file.close()
        in_file.close()












