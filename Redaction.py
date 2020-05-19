from datetime import datetime
import os
import glob


class Redaction:

    def __init__(self):
        """
        Creates a directory of files which is based on the current date and time
        Runs Bulk_Extractor on the attachments file which is related to the DTO

        | @param self: access the attributes of the class
        """
        # Created a folder which is named the current date and time
        self.date_time_obj = datetime.now()
        self.time_string = self.date_time_obj.strftime("%d-%b-%Y %H-%M-%S")
        self.directory = self.time_string
        self.parent_dir = r"C:\\Users\\angel\\OneDrive\\Documents\\Diss\\"
        self.full_directory_path = self.parent_dir + self.directory
        self.redactionbulk()
        self.removefiles(self.full_directory_path)

    def redactionbulk(self):
        """
        Runs Bulk_Extractor and outputs to the directory which has been created in the above function

        | @param self: access the attributes of the class
        """
        command = 'bulk_extractor -S ssn_mode=2 -o "' + self.full_directory_path + '" -R "C:\\Users\\angel\\PycharmProjects\\EWS-Plugin' \
                                                                '\\attachments"'
        os.system(command)

    def removefiles(self, full_directory_path):
        """
        Removes all of the files which have 0KB in them so that the program can ignore irrelevant files.
        It also removes the histogram files which aren't relevant since they don't have the right output for redaction.
        It removes the URL services which aren't relevant since they don't have the right output for redaction.
        It removes the XML Report since all the information that needs to be redacted is in the other files.

        | @param self: access the attributes of the class
        | @param fullDirectoryPath: Passes the full directory path
        """
        in_dir = full_directory_path
        os.chdir(in_dir)
        file_list = glob.glob("*.txt")

        for filename in file_list:
            # Removes all files which are 0KB since they have no information in them.
            if os.stat(filename).st_size == 0:
                os.remove(filename)

        for file_name in os.listdir(full_directory_path):
            try:
                string_parts = []
                # All histogram files are removed from the directory.
                str_file_name = str(file_name)

                string_parts.append(str_file_name.split("_"))
                for i in string_parts:
                    if "histogram.txt" in i:
                        os.remove(file_name)
            except IndexError:
                continue

        for file_name_services in os.listdir(full_directory_path):
            try:
                string_parts = []
                # All services files are removed from the directory.
                str_file_name = str(file_name_services)

                string_parts.append(str_file_name.split("_"))
                for i in string_parts:
                    if "services.txt" in i:
                        os.remove(file_name_services)
            except IndexError:
                continue

        if os.path.exists(full_directory_path):
            # Remove the report XML from the directory
            os.remove("report.xml")
        else:
            print("The file does not exist")

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

