import json_parser_module


class parser_module:
    json_parser = ""

    def __init__(self):
        """
        This is the main class which

        | @param self: access the attributes of the class
        """
        self.json_parser = json_parser_module.json_parser_module()

    def parse_ticket(self, ticket):
        """
        This is the main method of the class which is used as a wrapper class for the program.

        | @param self: access the attributes of the class
        | @param ticket: access the json ticket
        | @return: The json ticket
        """
        return self.json_parser.parse_ticket(ticket)
