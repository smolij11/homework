#!/usr/bin/env python
import sys


def parse_header(line):
    strings = line.split()

    if len(strings) < 4:
        print("error! correct header format: % id value description")
        return

    id = strings[1]
    print("ID: {}".format(id))

    value = strings[2]
    if value == "null" or value == "NULL" or value == "NaN" or value == "-":
        print("Value: {}".format(value))
    else:
        try:
            print("Value: {:.1f}".format(float(value)))
        except ValueError:
            print("Value: (wrong input format) {}".format(value))

    index = line.find(strings[2]) + len(strings[2])
    description = line[index:].strip()
    print("Description: {}".format(description))


def parse(lines):
    sequence_length = 0
    for line in lines:
        if line[0] == '%':
            if line != lines[0]:
                print("Sequence length: {}\n".format(sequence_length))
            parse_header(line)
            sequence_length = 0
            continue
        line = line.strip()
        sequence_length += len(line)
    print("Sequence length: {}\n".format(sequence_length))


def main():
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        file = open(arg,"r")
        lines = file.readlines()
        file.close()
        print("{}\n".format(arg))
        parse(lines)




#--------------------------
if __name__ == "__main__":
    main()
