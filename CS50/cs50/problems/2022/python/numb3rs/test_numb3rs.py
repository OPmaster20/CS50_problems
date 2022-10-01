from numb3rs import validate
def tt():
    assert validate('127.0.0.1')
    assert validate('255.255.255.255')
tt()