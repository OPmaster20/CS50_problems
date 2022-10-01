from plates import is_valid
def test_valid():
    assert is_valid('c')=='invalid'
def test_valid_false():
    assert is_valid('c')=='Valid'