import sqlite3
import new_campaign


def main():
    choices = {"new campaign": 0, "update campaign": 1}
    for choice in choices:
        print(f"Enter {choices[choice]} for {choice}")
        
    response = input("Enter your choice: ")
    print(f"You entered {response}")

    if response == "0":
        new_campaign.new_campaign()
    elif response == "1":
        print("Updating current campign")
        sqlite_loc = input("Enter db location")
    else:
        print("Invalid response")


if __name__ == "__main__":
    main()