from bank import value
def test_bank():
    assert value('Hello')=='$100'
def test_bank2():
    assert value('What’s up')=='$0'
def test_bank_true():
    assert value('Hi')=='$20'
