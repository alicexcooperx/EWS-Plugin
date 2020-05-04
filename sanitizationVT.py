import requests
import json


class SanitizationAV:

    def sanitiseAV(self, dto_object):

        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        api_key = '050e4c7768f9d896b852a271ed0718b0a87a24a7907a121337112dfcb3134bcd'
        files = []

        for file in dto_object.attachments:
            files.append({'file': (file, open(file, 'rb'))})

        for file in files:
            response = requests.post(url, files=file, params={"apikey": api_key})
            sha256_file = ""
            # print(response)
            output = json.loads(response.text)

            for item in output.items():
                if item[0] == 'sha256':
                    dto_object.attachments_hash.append(item[1])
                    # print("{0}: {1}".format(item[0], item[1]))
                    sha256_file = item[1]

            report_url = "https://www.virustotal.com/vtapi/v2/file/report"
            report_resp = requests.get(report_url, params={"apikey": api_key, "resource": sha256_file}).json()

            for index, value in report_resp.items():
                if index == "positives" and value == 0:
                    dto_object.attachments_virus.append(0)
                    # print("No Viruses Detected")
                elif index == "positives" and value > 0:
                    dto_object.attachments_virus.append(index['positives'])
                    # print("{0} positive results found".format(index['positives']))

# For each file in the directory,
# Upload it to virus total
# Get the hashes of each file and the name
# if a virus is found then returning the hash and it needs to be flagged
# put this into the DTO