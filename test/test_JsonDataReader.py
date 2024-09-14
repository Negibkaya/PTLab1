import pytest
from src.Types import DataType
from src.JsonDataReader import JsonDataReader
import json


class TestJsonDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "Иванов Константин Дмитриевич\n" + \
            " математика:91\n" + " химия:100\n" + \
            "Петров Петр Семенович\n" + \
            " русский язык:87\n" + " литература:78\n"
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        data = file_and_data_content[1]
        p = tmpdir.mkdir("datadir").join("my_data.json")
        with open(p, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
        return str(p), data

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
