# flake8: noqa

from pathlib import Path

import pytest

from tidypandas.read import locate_pattern


@pytest.fixture
def sample_text() -> str:
    return """name: max mustermann
        email: max.mustermann@gmail.com
        phone: +4915432944487
        address: musterweg 1, 12345 musterstadt"""


def test_locate_pattern_match(tmp_path: Path, sample_text: str) -> None:
    tmp_file = tmp_path / "sample_file.txt"
    tmp_file.write_text(sample_text)

    assert locate_pattern(tmp_file, "[+0][0-9]{8}") == 2


def test_locate_pattern_no_match(tmp_path: Path, sample_text: str) -> None:
    tmp_file = tmp_path / "sample_file.txt"
    tmp_file.write_text(sample_text)

    assert locate_pattern(tmp_file, "^$") == -1
