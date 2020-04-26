import Parser
# Wrapper Class - Just opens the JSON Ticket and hands it off to the parser.
# Can be safely removed when integrating.


def main():
    ticket = open("ticket.json", "r")
    ticket_contents = ticket.read()
    ticket.close()
    parsing = Parser.Parser()
    DTOObject = parsing.parse_ticket(ticket_contents)
    # sanitise = sanitizationVT2.SanitizationAV()
    # sanitise.sanitiseAV("C:\\Users\\angel\\PycharmProjects\\EWS-Plugin\\attachments\\")
    print(DTOObject.attachments)


if __name__ == '__main__':
    main()
