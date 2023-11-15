import time 

def introduction():
    print("Welcome to the Adventure Quest!")
    time.sleep(1)
    print("You find yourself in a mysterious land full of challenges and opportunities.")
    time.sleep(1)
    print("Your goal is to reach the treasure at the end of the quest.")
    time.sleep(1)

def make_choice(options): #функції make_choice надається параметр options
    print("Choose your action:")
    for i, option in enumerate(options, 1): #перебирається кожен елемент і номерується від 1
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options): #якщо користувачч вводить цифру між 1 і довжиною options, повертається вибір 
                return choice
            else: #інакше виводиться помилка
                print("Invalid choice. Try again.") 
        except ValueError: #виключення - якщо вводиться неправильний тип даних, то вивдиться зауваження
            print("Invalid input. Enter a number.")

def forest():
    print("You enter a dark forest.")
    time.sleep(1)
    print("Options:")
    time.sleep(0.5)
    print("1. Follow the path deeper into the forest.")
    print("2. Turn back and leave the forest.")

    choice = make_choice(["Follow the path", "Turn back"])
    # викликається функція разом зі списком даних опцій

    if choice == 1:
        print("As you follow the path, you encounter a group of friendly elves.")
        time.sleep(1)
        print("They offer to guide you through the forest.")
        time.sleep(1)
        print("Congratulations! You safely navigate the forest with the help of the elves.")
        return True
    else:
        print("You decide to leave the forest and explore other areas.")
        return False

def cave():
    print("You discover a mysterious cave.")
    time.sleep(1)
    print("Options:")
    time.sleep(0.5)
    print("1. Enter the cave.")
    print("2. Ignore the cave and continue exploring.")

    choice = make_choice(["Enter the cave", "Ignore the cave"])

    if choice == 1:
        print("You cautiously enter the cave.")
        time.sleep(1)
        print("Inside the cave, you find a hidden passage.")
        time.sleep(1)
        print("You discover a shortcut to the treasure!")
        return True
    else:
        print("You decide to ignore the cave and explore other areas.")
        return False

def treasure():
    print("You finally reach the treasure room!")
    time.sleep(1)
    print("Congratulations! You have completed the adventure and found the treasure.")

def main():
    introduction()

    # Start the adventure
    if forest():
        # If the player successfully navigates the forest, proceed to the next stage
        if cave():
            # If the player discovers the shortcut in the cave, proceed to the treasure
            treasure()
        else:
            print("You continue your quest in search of the treasure.")
    else:
        print("Your adventure ends as you leave the forest.")

if __name__ == "__main__":
    main()