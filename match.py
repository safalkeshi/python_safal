name = input("whats your name")
match name:
    case"harry":
        print("gryfindor")
    case"ron":
        print("slytherin")
    case _:
        print("who?")