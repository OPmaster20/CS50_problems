def main():
    x=str(input("Greeting:"))
    y=value(x)
    print(y)
def value(greeting):
    match greeting:
        case 'Hello' | 'Hello there' | 'Hello,Newman':
            return '$0'
        case 'Hey' | 'Hi' | 'How you doing':
            return '$20'
        case _:
            return '$100'
if __name__ == "__main__":
    main()