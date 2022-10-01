from validator_collection import validators, checkers, errors
address=input("what's you email address? ").strip()
is_email_address = checkers.is_email(address)
if is_email_address:
    print('Valid')
else:
    print('Invalid')
