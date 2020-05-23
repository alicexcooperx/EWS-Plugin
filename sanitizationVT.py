import requests
import json


class sanitize_module:

    def sanitise_av(self, dto_object):
        """
        Uploads Files from a specific folder which is scanned via the VirusTotal API it is then returned and appended
        to the DTO with a value depending if a virus is found or not.

        | @param self: access the attributes of the class
        | @param dto_object: the values depending on the virus detection can be stored in the DTO
        """
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        api_key = '050e4c7768f9d896b852a271ed0718b0a87a24a7907a121337112dfcb3134bcd'
        files = []

        # Getting each file which is in the attachments folder
        for file in dto_object.attachments:
            files.append({'file': (file, open(file, 'rb'))})

        for file in files:
            # For files in attachments upload to the API and keep the sha256 variable ready to be filled.
            response = requests.post(url, files=file, params={"apikey": api_key})
            sha256_file = ""
            # print(response)
            output = json.loads(response.text)

            # Appends the SHA256 hash to the attachments_hash in the DTO.
            for item in output.items():
                if item[0] == 'sha256':
                    dto_object.attachments_hash.append(item[1])
                    # print("{0}: {1}".format(item[0], item[1]))
                    sha256_file = item[1]

            # Goes to the report of the specified hash in the code above
            report_url = "https://www.virustotal.com/vtapi/v2/file/report"
            report_resp = requests.get(report_url, params={"apikey": api_key, "resource": sha256_file}).json()

            # Changes values in the DTO depending if the virus comes back positive or not.
            for index, value in report_resp.items():
                if index == "positives" and value == 0:
                    dto_object.attachments_virus.append(0)
                    # print("No Viruses Detected")
                elif index == "positives" and value > 0:
                    dto_object.attachments_virus.append(index['positives'])
                    # print("{0} positive results found".format(index['positives']))