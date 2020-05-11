import JSONParser


class Parser:
    json_parser = ""

    def __init__(self):
        """
        This is the main class which

        | @param self: access the attributes of the class
        """
        self.json_parser = JSONParser.JSONParser()

    def parse_ticket(self, ticket):
        """
        This is the main method of the class which is used as a wrapper class for the program.

        | @param self: access the attributes of the class
        | @param ticket: access the json ticket
        | @return: The json ticket
        """
        return self.json_parser.parse_ticket(ticket)
