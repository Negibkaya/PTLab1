# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from JsonDataReader import JsonDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    readerJson = JsonDataReader()
    students = readerJson.read(path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    lateStudents = CalcRating(students).calculate_late_students()
    print("Rating: ", rating)
    print("Late students: ", lateStudents)


if __name__ == "__main__":
    main()
