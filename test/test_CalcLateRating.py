# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcLateRating import CalcLateRating
import pytest
RatingsType = dict[str, float]


class TestCalcRating:
    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
            [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович":
            [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ]
        }
        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000
        }
        return data, rating_scores

    def test_calculate_late_students(self,
                                     input_data: tuple[DataType,
                                                       RatingsType]) -> None:
        rating = CalcLateRating(input_data[0]).calculate_late_students()
        assert rating == 1
