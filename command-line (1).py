import time
from datetime import datetime
from deep_translator import GoogleTranslator
import pyttsx4

# Set the password
password = "password123"

linux_version = 19.97
lang = ''
ttt = ''  # text to translate
settings = ""

os = str(input("What os do you want? "))
guestname = input("What is this device's name? ")



# Prompt for password
while True:
    entered_password = input("Enter password: ")
    if entered_password == password:
        break
    else:
        print("Incorrect password. Try again.")

while True:
    print("Type 'help' for help.")
    time.sleep(0.25)
    command = input(guestname + "_$ ")
    if command.lower() == "help":
        print("Type 'calculator' to open the calculator.\n"
              "Type 'power off' to shut down the computer.\n"
              "Type 'linux --version' to see the version of Linux.\n"
              "Type 'time' to see what time it is.\n"
              "Type 'translator' to translate text")

    elif command.lower() == "":
        print("Please enter a command. Type 'help' for available commands.")

    elif command.lower() == "linux --version":
        print("Linux version: " + str(linux_version), "pyhelper" + " (" + os + ")")

    elif command.lower() == "power off":
        print("The computer will turn off in 5 secs\n")
        time.sleep(5)
        break

    elif command.lower() == "tts":
        print("in development")

    elif command.lower() == 'settings':
        print("You can edit the device name by typing 'edevicename'\n"
              "You can edit the os by typing 'edeviceos'")
        settings = str(input("Choose a setting to edit: "))

        if settings == "edevicename":
            print("Current: " + guestname)
            guestname = input("Set device name to: ")
            print("The new name is set!")

        elif settings == "edeviceos":
            print("Current: " + os)
            os = input("Change os to: ")
            print("The new os is set!")

    elif command.lower() == "translator":
        print("DO NOT TYPE IN THE FULL NAME OF THE LANGUAGE, write it in a shortcut ex: de, en")
        try:
            lang = input('What language do you want? ')
            ttt = input("What do you want to translate ")
            translated = GoogleTranslator(source='auto', target=lang).translate(ttt)
            print("The translation is: ", translated)
        except:
            print("ERROR please try again later")

    elif command.lower() == "time":
        print("it's the " + str(datetime.now()) + " o'clock")

    elif command.lower() == "calculator":
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator: ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            print("Invalid operator.")
            continue

        print("Result: " + str(result))
    else:
        print("bash: " + command + ":" + " Command not found" + ", Type 'help' for assistance")
