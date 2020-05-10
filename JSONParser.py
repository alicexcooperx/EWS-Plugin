import json
import DTO
import os
import sanitizationVT


class JSONParser:

    def parse_ticket(self, ticket):
        """
        This is the JSONParser class which takes in the original ticket and passes certain values below into the Data
        Transfer Object.

        | @param self: access the attributes of the class
        | @param ticket: The ticket which is submitted by the user in the EWS.
        """
        payload = json.loads(ticket)

        attribute_values = payload["attributeValues"]
        organization_id = payload["organizationId"]
        creator_id = payload["creatorId"]
        description = payload["description"]
        comments = payload["comments"]
        local_organization_ticket_info = payload["localOrganizationTicketInfos"]
        references = payload["references"]
        title = payload["title"]
        cyber_ticket_info = payload["cyberticketEmails"]

        attachments = []

        for test in payload["attachments"]:
            attachments.append(test["filename"])

        ticket_heading = payload["title"]
        sub_directory = ticket_heading
        ticket_creator = payload["creatorId"]
        directory = ticket_creator

        path = ("C:\\Users\\angel\\PycharmProjects\\EWS-Plugin\\" + directory + "\\" + sub_directory)
        # attachments_folder = "C:\\Users\\angel\\PycharmProjects\\EWS-Plugin\\attachments\\"

        try:
            os.makedirs(path)
        except OSError:
            print("Creation of directory %s failed" % path)
        else:
            print("Successfully created the directory %s" % path)

        dtoObject = DTO.DTO(title, description, creator_id, organization_id, comments, references,
                            local_organization_ticket_info, cyber_ticket_info, attribute_values, attachments)

        return dtoObject
