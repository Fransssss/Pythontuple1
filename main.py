# tudle = group related data that cannot be changed
import datetime

personOne = ["Andy", 19, "Running"]
personTwo = ["Bandy", 20, "Swimming"]

print("\n== Tuple Practice ==")
print("1. Display data")
print("2. Count how many times a word exist")
print("3. Locate an index of a word")
print("E. Exit")
choice = input("choice: ")

while choice != "e" and choice != "E":
    if choice == "1":
        print('\n')
        print(personOne)
        print(personTwo)
    elif choice == "2":
        person = input("\ta.1st person\n\tb.2nd person\n\tperson: ")
        if person == 'a':
            word = input("\tinput a word to count: ")
            print("\tCount: " + str(personOne.count(str(word))))               # count how many time a word exist
        elif person == 'b':
            word = input("\tinput a word to count: ")
            print("\tCount: " + str(personTwo.count(str(word))))
        else:
            print("invalid input")
    elif choice == "3":
        person = input("\ta.1st person\n\tb.2nd person\n\tperson: ")
        if person == 'a':
            word = input("\tinput a word to locate: ")
            print("\tLocation: " + str(personOne.index(word)))                 # locate the index of a word
        elif person == 'b':
            word = input("\tinput a word to locate: ")
            print("\tLocation: " + str(personTwo.index(word)))
        else:
            print("\tinvalid input")
    else:
        print("\n[invalid input]")

    print("\n== Tudle Practice ==")
    print("1. Display data")
    print("2. Count how many times a word exist")
    print("3. Locate an index of a word")
    print("E. Exit")
    choice = input("choice: ")

if choice == "e" or choice == "E":
    print("\n== Exit Program ==")
