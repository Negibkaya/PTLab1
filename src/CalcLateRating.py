# -*- coding: utf-8 -*-
# from Types import DataType
from .Types import DataType

RatingType = dict[str, float]


class CalcLateRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calculate_late_students(self) -> RatingType:
        count = 0
        for subjects in self.data.values():
            is_late = any(score <= 61 for _, score in subjects)
            if is_late:
                count += 1
        return count
