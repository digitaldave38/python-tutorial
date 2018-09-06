#!/usr/bin/env python3.6
def age_in_seconds():
    user_age = input("Enter your Age: ")
    age_seconds = int(user_age) * 365 * 24 * 60 * 60
    print("You have lived for {} seconds.".format(age_in_seconds))

if __name__ == '__main__':
    age_in_seconds()

