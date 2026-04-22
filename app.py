def test_basic_math():
    assert 1 + 1 == 2

def test_string_ops():
    name = "jenkins"
    assert name.upper() == "JENKINS"

def test_list_ops():
    items = [1, 2, 3]
    assert len(items) == 3
