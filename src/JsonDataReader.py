# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import json


class JsonDataReader(DataReader):
    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Преобразование данных в нужный формат
        students: DataType = {}
        for student, subjects in data.items():
            students[student] = [(subj, score)
                                 for subj, score in subjects.items()]

        return students
