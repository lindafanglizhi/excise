
import pytest

CONTENT = "content"


def test_create_file(tmp_path):
    d = tmp_path/ "sub"
    d.mkdir()
    p = d / "hello1.txt"
    print(p)
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    print(tmp_path.iterdir())
    assert len(list(tmp_path.iterdir())) == 1
    # assert 0

