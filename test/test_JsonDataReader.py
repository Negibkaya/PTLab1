import pytest
from src.Types import DataType
from src.JsonDataReader import JsonDataReader
import json


class TestJsonDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        data = {
            "Иванов Иван Иванович": {
                "математика": 67,
                "литература": 100,
                "программирование": 91
            },
            "Петров Петр Петрович": {
                "математика": 78,
                "химия": 87,
                "социология": 61
            }
        }
        expected_data = {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }
        return json.dumps(data, ensure_ascii=False), expected_data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        json_content, expected_data = file_and_data_content
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(json_content, encoding='utf-8')
        return str(p), expected_data

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
