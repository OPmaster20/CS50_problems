x=str(input("Greeting:"))
match x:
    case 'Hello' | 'Hello there' | 'Hello,Newman':
        print('$0')
    case 'Hey' | 'Hi' | 'How you doing':
        print('$20')
    case _:
        print('$100')