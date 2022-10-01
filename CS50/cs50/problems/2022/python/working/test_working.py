from working import convert
def test():
    assert convert("10:30 PM to 8:50 AM")=='22:30 to 08:50'
    assert convert("9:00 AM to 5:00 PM")=='09:00 to 17:00'
    test_2()
def test_2():
    assert convert("9:60 AM to 5:60 PM")=='09:60 to 17:60'
test()