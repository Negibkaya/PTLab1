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

    # Рассчет студентов с академической задолженностью
    def calculate_late_students(self) -> RatingType:
        count = 0
        for student, subjects in self.data.items():
            is_late = any(score <= 61 for _, score in subjects)
            if is_late:
                count += 1
        return count
