#!/usr/bin/env python
import sys

# parse a single header
def parse_header(line):
    strings = line.split()

    # check if the header is ok
    if len(strings) < 4:
        print("error! correct header format: % id value description")
        return

    # get id
    id = strings[1]
    print("ID: {}".format(id))

    # get numeric value, also do some check if the value is ok (int, float, "null", "NULL", "NaN", "-")
    value = strings[2]
    if value == "null" or value == "NULL" or value == "NaN" or value == "-":
        print("Value: {}".format(value))
    else:
        try:
            print("Value: {:.1f}".format(float(value)))
        except ValueError:
            print("Value: (wrong input format) {}".format(value))

    # get description
    index = line.find(strings[2]) + len(strings[2])
    description = line[index:].strip()
    print("Description: {}".format(description))

# parse a single file
def parse(lines):
    sequence_length = 0

    for line in lines:
        if line[0] == '%':
            if line != lines[0]:
                print("Sequence length: {}\n".format(sequence_length))
            parse_header(line)  # parse a header
            sequence_length = 0
            continue

        line = line.strip()
        sequence_length += len(line)

    print("Sequence length: {}\n".format(sequence_length))


# main function
def main():
    for arg in sys.argv:
        # skip ./parse.py
        if arg == sys.argv[0]:
            continue
        # handle file errors
        try:
            file = open(arg,"r")
            lines = file.readlines()
            file.close()
        except:
            print("error opening, reading or closing file {}.\n".format(arg))
            continue

        # print file name and parse file
        print("{}\n".format(arg))
        parse(lines)




#--------------------------
if __name__ == "__main__":
    main()
