import json
import DTO
# Imported JSON to make it so that the ticket could be loaded in JSON.
# Imported DTO so the object could be instansiated

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

        dto_object = DTO.DTO(title, description, creator_id, organization_id, comments, references,
                            local_organization_ticket_info, cyber_ticket_info, attribute_values, attachments)

        return dto_object
