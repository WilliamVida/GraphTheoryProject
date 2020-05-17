import thompsons
import argparse


parser = argparse.ArgumentParser(description="Compare a regular expression to a string")
parser.add_argument("-r", "--regex", type=str,metavar="", help="Regular Expression")
parser.add_argument("-s", "--s", type=str, metavar="",  help="String")
args = parser.parse_args()


def testing(regex, s):
    result = thompsons.match(regex, s)
    return result


if __name__ == "__main__":
    print(thompsons.match(args.regex, args.s))
