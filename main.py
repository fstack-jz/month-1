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
                 ": ")
    age = input("Please enter your current age\n"
                ": ")
    def age_checker():
        while True:
            age = input("Please enter your current age\n"
                        ": ")
            if age == int:
                age = age
            else: 
                print("Please enter your age as a number.")
    age = age_checker
    occupation = input("Enter your current occupation\n"
                       ": ")
    place_of_work_or_study = input("In?\n"
                                   ": ")

    print(f"\nGreetings!, {name}!, You are currently {age} years old and a {occupation} in {place_of_work_or_study}!")

main()