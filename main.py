# PROJECT 1 CALCULATOR


import time as t
import sys as s

def tpwrtr(text, delay=0.09):
    for char in text:
        s.stdout.write(char)
        s.stdout.flush()
        t.sleep(delay)
    print()

def main():
    name = input("What is your name?\n"
                 ": ").upper()
    while True:
        age = input("What is your age?\n" \
        ": ")
        if age.isdigit():
            break
        else:
            print("Please enter a number only.")
    occupation = input("Enter your current occupation\n"
                       ": ").upper()
    place_of_work_or_study = input("In?\n"
                                   ": ").upper()
    

    print("-----User Interface-----")
    print(f"\nGreetings!, {name}!, you are currently {age} and a {occupation} in {place_of_work_or_study}\n")
    print("------------------------")

main()