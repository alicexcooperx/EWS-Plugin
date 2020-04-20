# Wrapper Class - Just opens the JSON Ticket and hands it off to the parser.
# Can be safely removed when integrating.


def main():
    ticket = open("ticket.json", "r")
    ticket_contents = ticket.read()
    ticket.close()
    print(ticket_contents)


if __name__ == '__main__':
    main()
