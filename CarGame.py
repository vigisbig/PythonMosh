command = ""

while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - To quit""")
    elif command == "quit":
        break
    else:
        print("I don't understand that")
