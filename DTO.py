class DTO:
    def __init__(self, title, description, creator_id, organization_id, comments, references,
                 local_organization_ticket_info, cyber_ticket_info, attribute_values, attachments):
        self.attribute_values = attribute_values
        self.organization_id = organization_id
        self.creator_id = creator_id
        self.description = description
        self.comments = comments
        self.local_organization_ticket_info = local_organization_ticket_info
        self.references = references
        self.title = title
        self.cyber_ticket_info = cyber_ticket_info
        self.attachments = attachments