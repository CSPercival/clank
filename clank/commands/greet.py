def greet_init_parser(parser):
    subparser = parser.add_parser("greet", help="Print greeting message")

def greet():
    print("Hello, my name is Clank.")
    print("What can I do for you?")