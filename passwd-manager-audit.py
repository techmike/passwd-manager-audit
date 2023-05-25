import csv
import argparse
import sys

ONEPASSLIST = []
LASTPASSLIST = []
VERBOSE=False

def parseonepass(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            #print(row['first_name'], row['last_name'])
            onekey = f"{row['Title']}-{row['Url']}-{row['Username']}-{row['Password']}"
            if onekey in ONEPASSLIST:
                pass
            else:
                ONEPASSLIST.append(onekey)

def parselastpass(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            #print(row)
            #print(row['first_name'], row['last_name'])
            #lastkey = f"{row['name']}-{row['url']}-{row['username']}-{row['grouping']}"
            lastkey = f"{row['name']}-{row['url']}-{row['username']}-{row['password']}"
            print(lastkey)
            if lastkey in LASTPASSLIST:
                pass
            else:
                LASTPASSLIST.append(lastkey)

def report():
    print(f"1password has {len(ONEPASSLIST)}\nLastpass has {len(LASTPASSLIST)}")
    COUNTNOTIN = 0
    for p in ONEPASSLIST:
        if p in LASTPASSLIST:
            pass
        else:
            COUNTNOTIN += 1
            print(p)

    print(f"{COUNTNOTIN} creds not in LASTPASS")


def main():
    parseonepass()
    parselastpass()
    print(f"1password has {len(ONEPASSLIST)}\nLastpass has {len(LASTPASSLIST)}")
    COUNTNOTIN = 0
    for p in ONEPASSLIST:
        if p in LASTPASSLIST:
            pass
        else:
            COUNTNOTIN += 1
            print(p)

    print(f"{COUNTNOTIN} creds not in LASTPASS")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true', help="Increase output verbosity")
    parser.add_argument('--lastpass-file', dest='lastpass_file', help='provide the lastpass file')
    parser.add_argument('--onepassword-file', dest='onepassword_file',  help='provide the 1password file')
    # type=argparse.FileType('r'),
    args = parser.parse_args()

    if args.verbose:
        VERBOSE=True

    if args.lastpass_file or args.onepassword_file:
        if args.lastpass_file:
            parselastpass(args.lastpass_file)

        if args.onepassword_file:
            parseonepass(args.onepassword_file)
    else:
        parser.print_help()
        sys.exit(1)

    report()

