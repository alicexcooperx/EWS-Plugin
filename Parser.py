import JSONParser


class Parser:
    json_parser = ""

    def __init__(self):
        self.json_parser = JSONParser.JSONParser()

    def parse_ticket(self, ticket):
        return self.json_parser.parse_ticket(ticket)
