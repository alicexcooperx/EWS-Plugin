import Parser
import sanitizationVT


def main():
    """
    This is the main method which is used as a wrapper class for the program.

    | @param: None
    """
    ticket = open("ticket.json", "r")
    ticket_contents = ticket.read()
    ticket.close()
    parsing = Parser.Parser()
    dto_object = parsing.parse_ticket(ticket_contents)
    sanitise = sanitizationVT.SanitizationAV()
    sanitise.sanitiseAV(dto_object)

if __name__ == '__main__':
    main()
