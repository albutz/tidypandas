# flake8: noqa

from pathlib import Path

import pandas as pd
import pytest

from tidypandas import read_sub
from tidypandas.read import PatternNotFoundError, locate_pattern


@pytest.fixture
def sample_text() -> str:
    return (
        "name: max mustermann\n"
        "email: max.mustermann@gmail.com\n"
        "phone: +4915432944487\n"
        "address: musterweg 1, 12345 musterstadt\n"
    )


@pytest.fixture
def sample_csv_sub() -> str:
    return (
        "key_1,val_1\n"
        "key_2,val_2\n"
        "\n"
        "2022/05/07\n"
        "\n"
        "y,x_1,x_2\n"
        "0,low,0.989\n"
        "1,medium,-1.923"
    )


@pytest.fixture
def sample_csv_no_sub() -> str:
    return "y,x_1,x_2\n" "0,low,0.989\n" "1,medium,-1.923"


@pytest.fixture
def df_expected() -> pd.DataFrame:
    return pd.DataFrame({"y": [0, 1], "x_1": ["low", "medium"], "x_2": [0.989, -1.923]})


def test_locate_pattern_match(tmp_path: Path, sample_text: str) -> None:
    tmp_file = tmp_path / "sample_file.txt"
    tmp_file.write_text(sample_text)

    assert locate_pattern(tmp_file, "[+0][0-9]{8}") == 2


def test_locate_pattern_no_match(tmp_path: Path, sample_text: str) -> None:
    tmp_file = tmp_path / "sample_file.txt"
    tmp_file.write_text(sample_text)

    assert locate_pattern(tmp_file, "^$") == -1


def test_locate_pattern_raw_string(sample_text: str) -> None:
    assert locate_pattern(sample_text, "[+0][0-9]{8}") == 2


def test_locate_pattern_raw_string_no_match(sample_text: str) -> None:
    assert locate_pattern(sample_text, "^$") == -1


def test_read_sub_pattern_found(
    tmp_path: Path, sample_csv_sub: str, df_expected: pd.DataFrame
) -> None:
    tmp_file = tmp_path / "sample_csv.csv"
    tmp_file.write_text(sample_csv_sub)

    pd.testing.assert_frame_equal(
        read_sub(tmp_file, "(?=.*y)(?=.*x_1)(?=.*x_2)", index_col=False), df_expected
    )


def test_read_sub_pattern_found_no_sub(
    tmp_path: Path, sample_csv_no_sub: str, df_expected: pd.DataFrame
) -> None:
    tmp_file = tmp_path / "sample_csv.csv"
    tmp_file.write_text(sample_csv_no_sub)

    pd.testing.assert_frame_equal(
        read_sub(tmp_file, "(?=.*y)(?=.*x_1)(?=.*x_2)", index_col=False), df_expected
    )


def test_read_sub_pattern_not_found(tmp_path: Path, sample_csv_sub: str) -> None:
    tmp_file = tmp_path / "sample_csv.csv"
    tmp_file.write_text(sample_csv_sub)

    with pytest.raises(PatternNotFoundError) as excinfo:
        read_sub(tmp_file, "(?=.*x_3)(?=.*x_4)", index_col=False)
    assert "Pattern could not be found." == str(excinfo.value)
