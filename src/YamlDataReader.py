import yaml
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        # Преобразование данных в нужный формат
        students: DataType = {}
        for student, subjects in data.items():
            students[student] = [(subj, score)
                                 for subj, score in subjects.items()]

        return students
