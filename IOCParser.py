import re, argparse, os, sys, logging

# This is setting the absolute path file for python file
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)


class MyIOC:
    # a simple class with a value for the type (kind) of IOC and the actual value of the IOC.
    # def is defining a function name
    # self means that it has access to all the variables (or scope) so all the variable that have self. will be global
    # put self in the function header before anything else if you need to use something globally.
    # init is like the main method in java
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value


def check(kind):
    file = "{}/data/{}".format(dir_path, kind)
    file_type = open(file, "r")
    y = []
    for line in file_type:
        y.append(line.rstrip())
    file_type.close()
    return "|".join(y)[:-1]


class Parser:
    # takes a text and returns IOCs found in that text as a list of IOC-objects.
    # TLDs is domains
    # re.compile is regular expressions operations matching

    # The regex for IP goes as follows: 0-9, makes sure 3 numbers no more for each section
    ipReg = ["IP Address", re.compile(r'(([0-9]{1,3}\.){3}[0-9]{1,3})')]
    # for URL // means one backslash
    uriReg = ["uri",
              re.compile('\\b((http.:\\/\\/)?[a-zA-Z0-9\\.]{2,}[\\.](?:' + check("tlds") + ')(\\/[\\S]*)*)\\b', re.I)]
    # 32 characters long
    md5Reg = ["md5", re.compile(r'\b(([a-f0-9]{32}\b|\b[A-F0-9]{32}))\b')]
    # 40 characters long
    sha1Reg = ["sha1", re.compile(r'\b(([a-f0-9]{40}\b|\b[A-F0-9]{40}))\b')]
    # 64 characters long
    sha256Reg = ["sha256", re.compile(r'\b(([0-9a-z]{64}\b|\b[0-9A-Z]{64}))\b')]
    # starts with CVE then - year - arbitary digits
    CVEReg = ["CVE", re.compile(r'\b((CVE[\-]?[0-9]{4}\-[0-9]{3,6}))\b')]
    # all numbers and letters can be upper and lower before @ then same goes for ones after, and then .co being 2 .
    # after being 6 max
    emailReg = ["email", re.compile(r'\b(([a-zA-Z0-9\+\_\-]+[@][a-zA-Z0-9\+\_\-]+[.][a-zA-Z]{2,6}))\b')]
    #
    fileReg = ["filename", re.compile('(([a-zA-Z0-9\\.-_])+[\\.](' + check("extensions") + '))\\b', re.I)]

    def __init__(self, text):
        self.text = re.sub(r"\[\.\]", r".", text)
        self.text = re.sub(r'hxxp', r'http', self.text)

    def parse(self):
        iocs = []
        # putting regex into an array
        regexes = [self.ipReg, self.uriReg, self.md5Reg, self.sha1Reg, self.sha256Reg, self.CVEReg,
                   self.emailReg, self.fileReg]
        # loops around the reg exes and outputs to user
        for regex in range(len(regexes)):
            logging.debug("scanning for {}s".format(regexes[regex][0]))
            rule = []
            raw_rule = regexes[regex][1].findall(self.text)
            # raw rule takes the regex and find all currencies that match it in self.text,
            # this adds the occurrence it found to the rule array
            for x in range(len(raw_rule)):
                rule.append(raw_rule[x][0])
            # this adds the occurrence it round for IOC and adds to rule array
            for j in range(len(rule)):
                iocs.append(MyIOC(regexes[regex][0], rule[j]))
                logging.debug("Adding {} as a {}".format(rule[j], regexes[regex][0]))
        # this adds the occurrence for the type
        for regex in range(len(iocs)):
            logging.debug("IOC-type: {}\t\tIOC-value: {}".format(iocs[regex].kind, iocs[regex].value))
            logging.info("Found {} IOCs.".format(len(iocs)))
        return iocs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="IOC-parser extracts Indicators of Compromise (IOC) from a given plaintext source and exports "
                    "them to a simple .csv-file.")

    parser.add_argument('-s', '--source', metavar='inputfilename',
                        dest='source', action='store', required=True,
                        help='the sourcefile you want to scrape IOCs from.')

    parser.add_argument('-o', '--output', metavar='outputfilename',
                        dest='destination', action='store', required=True,
                        help='the filename you want to save to. something.csv would make the most sense.')

    args = parser.parse_args()
    logging.info("Starting Parser")

    f = open(args.source, "r")
    logging.info("opened {} for Parsing".format(args.source))
    resultsObject = Parser(f.read())
    results = resultsObject.parse()
    f.close()
    logging.info("Read and closed {}.".format(args.source))

    g = open(args.destination, "w")
    logging.info("Opened {} to safe results.".format(args.destination))
    for i in range(len(results)):
        g.write("{},{}\n".format(results[i].kind, results[i].value))
    g.close()
    logging.info("Closed {}.".format(args.destination))
    logging.info("Finishing Parser")
