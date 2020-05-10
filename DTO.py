class DTO:

    def __init__(self, title, description, creator_id, organization_id, comments, references,
                 local_organization_ticket_info, cyber_ticket_info, attribute_values, attachments):
        """
        This is the DTO object which stores relevant information about the incoming ticket.

        | @param self: access the attributes of the class
        | @param title: Title of the ticket
        | @param description: Description of the ticket
        | @param creator_id: Creator of the ticket
        | @param organization_id: Organisation that created the ticket
        | @param comments: Comments in the ticket
        | @param references: References related to the ticket
        | @param local_organization_ticket_info: Local information of the organisation
        | @param cyber_ticket_info: Information about the ticket e.g. attributes
        | @param attribute_values: Values within the attribute
        | @param attachments: Attachments which are in the ticket
        """
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
        self.attachments_hash = []
        self.attachments_virus = []
