# -*- coding: utf-8 -*-
import argparse
import sys
from .CalcRating import CalcRating
from .CalcLateRating import CalcLateRating
from .JsonDataReader import JsonDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader_json = JsonDataReader()
    students = reader_json.read(path)
    print("Students: ", students)

    calc_rating = CalcRating(students)
    rating = calc_rating.calc()

    calc_late_students = CalcLateRating(students)
    late_students = calc_late_students.calculate_late_students()

    print("Rating: ", rating)
    print("Late students: ", late_students)


if __name__ == "__main__":
    main()
