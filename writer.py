#!/usr/bin/env python
import sys

# write the sequence with maximum line length
def write_with_wrap(sequence_string,output,line_length):
    lines = [sequence_string[i:i+line_length] for i in range(0, len(sequence_string), line_length)]
    for line in lines:
        output.write("{}\n".format(line))

def main():
    output_file = ""
    line_length = 100
    input_files = []

    # get output file, line wrap and input files in one cycle
    for i,arg in enumerate(sys.argv):
        if arg == sys.argv[0] or sys.argv[i-1] == "--output" or sys.argv[i-1] == "--wrap":
            continue
        if arg == "--output":
            try:
                output_file = sys.argv[i+1]
            except:
                print("after --output argument, there should be an output file specified!")
                exit()
            continue
        if arg == "--wrap":
            try:
                line_length = int(sys.argv[i + 1])
            except:
                print("after --wrap argument, there should be an integer!")
                exit()
            continue
        input_files.append(arg)

    output = open(output_file,"w+")

    # open all input files & write into the new output file
    for f in input_files:
        try:
            file = open(f,"r")
            lines = file.readlines()
        except:
            print("could not open file {}!".format(f))
            continue
        file.close()

        sequence_string = ""  # whole sequence in 1 string
        for line in lines:
            
            if line[0] == "%":
                if line != lines[0]:
                    write_with_wrap(sequence_string,output,line_length)
                output.write(line)
                sequence_string = ""
                continue

            sequence_string += line.strip()

        # do last entry
        write_with_wrap(sequence_string, output, line_length)


    output.close()


#--------------------------
if __name__ == "__main__":
    main()