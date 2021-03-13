from entrance import Entrance

if __name__ == "__main__":
    print("Starting DrawSwap server!")

    e = Entrance()
    e.start()
    e.accept_incoming_connections()
