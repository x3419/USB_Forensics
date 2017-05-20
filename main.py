__author__ = "Alex Bernier"
__date__ = "5/19/17"
__version__ = 1.0
__description__ = "Investigates setupapi.dev.log for USB device history"

import argparse
import os


def printOutput(set_of_tuples):

    for data,date in set_of_tuples:
        print "Device: " + data
        print "Date: " + date + "\n"

def parse_stuff(file_name):

    """
    Parses the setupapi.dev.log ile
    :return:
    """

    if not os.path.isfile(file_name):
        print "File not found"
        exit()

    output_set = set()

    with open(file_name) as lines:
        for i,line in enumerate(lines):
            # if the line we're looking for is a USB entry, save the USB data and date of insertion into vars and then print
            if "device install (hardware initiated)" in line.lower() and \
                            line.split("-")[1].strip().strip("]").split("\\")[0] == "USB":
                line_split_strip = line.split("-")[1].strip().strip("]")  # line[1] is our juicy data
                next_line = next(lines)
                date = next_line.split(" ")[4].strip() + " " + next_line.split(" ")[5].strip()

                vid = line_split_strip.lower().split("vid_")[1].split("&")[0]
                #pid = line_split_strip.lower().split("pid_")[1].split("&")[0]
                print(pid)

                output_set.add( (line_split_strip,date) ) # add tuple to a set - force unique entries

    printOutput(output_set)


def main(arguments):

    """
    Runs our program
    :return: Nothing
    """

    file_name_path = "{}\\setupapi.dev.log".format(arguments.d)

    print "{:=^20}".format("")
    print "Parser version " + str(__version__)
    print "{:=^20}".format("")

    parse_stuff(file_name_path)


if __name__ == "__main__":

    description = 'Parses the setupapi.dev.log located in C:\Windows\INF by default'
    epilog = 'Built by Alex Bernier, reading "Learning Python for Forensics"'

    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    parser.add_argument('-d', help='directory of log file', default='C:\\Windows\\INF')  # Optional argument, file path

    arguments = parser.parse_args()

    main(arguments)