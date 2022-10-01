from um import count
def test_falid1():
    assert count('yumy')==0
def test_falid2():
    assert count('werum')==0
def test_true():
    assert count('um?')==1