import json
import requests


class VirusTotalSanitize:

    def sanitisevt(self):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        api_key = '050e4c7768f9d896b852a271ed0718b0a87a24a7907a121337112dfcb3134bcd'
        files = {'file': ('C:\\Users\\angel\\OneDrive\\Documents\\Diss\\16-Apr-2020 13-17-51\\domain.txt',
                          open('C:\\Users\\angel\\OneDrive\\Documents\\Diss\\16-Apr-2020 13-17-51\\domain.txt', 'rb'))}
        # make it recurse through a directory of files instead of just one file.
        response = requests.post(url, files=files, params={"apikey": api_key})
        sha256_file = ""
        print(response.json())
        output = json.loads(response.text)

        for i in output.items():
            if i[0] == 'sha256':
                print("{0}: {1}".format(i[0], i[1]))
                sha256_file = i[1]

        report_url = "https://www.virustotal.com/vtapi/v2/file/report"
        report_resp = requests.get(report_url, params={"apikey": api_key, "resource": sha256_file}).json()
        for index, value in report_resp.items():
            if index == "positives" and value == 0:
                # If no viruses are found then DTO is returned without any changes same as attachments.
                print("No Viruses Detected")
            elif index == "positives" and value > 0:
                # have this so it returns the hash value in the report so that you can view the malicious code
                # without potentially accessing it or running it.
                print("{0} postive results found".format(index['positives']))
