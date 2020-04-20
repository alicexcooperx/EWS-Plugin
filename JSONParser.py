import json
import DTO


class JSONParser:

    def parse_ticket(self, ticket):
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
        attachments = payload["attachments"]

        DTOObject = DTO.DTO(title, description, creator_id, organization_id, comments, references,
                            local_organization_ticket_info, cyber_ticket_info, attribute_values, attachments)
        return DTOObject
