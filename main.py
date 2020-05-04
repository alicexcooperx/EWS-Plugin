import Parser
import sanitizationVT;
# Wrapper Class - Just opens the JSON Ticket and hands it off to the parser.
# Can be safely removed when integrating.


def main():
    ticket = open("ticket.json", "r")
    ticket_contents = ticket.read()
    ticket.close()
    parsing = Parser.Parser()
    dto_object = parsing.parse_ticket(ticket_contents)
    sanitise = sanitizationVT.SanitizationAV()
    sanitise.sanitiseAV(dto_object)
    # print(dto_object.attachments_hash)
    # print(dto_object.attachments_virus)

if __name__ == '__main__':
    main()
