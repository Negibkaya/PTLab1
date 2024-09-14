# -*- coding: utf-8 -*-
from Types import DataType
RatingType = dict[str, float]


class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        return self.rating

    @staticmethod
    def calculate_excellent_students(data: DataType) -> int:
        count = 0
        for student, subjects in data.items():
            is_excellent = all(score >= 90 for _, score in subjects)
            if is_excellent:
                count += 1
        return count
