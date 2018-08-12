#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This is a program to show you what you sold in the vending shop when you
   log back in the game"""

import csv
import datetime # This is for logging the current date in the shelf file
import shelve

def get_data_from_file(file_path):
    """Opens a CSV file and retrieves the data from it"""

def create_data_file(file_path):
    """Creates a CSV file with the data the user provided"""


if __name__ == '__main__':
    # Main method goes here
    print("Welcome to the market tracker!")
    print("""Please tell me which items you are vending right now.
             You can vend up to 12 items in your personal shop.""")
    vending_items = dict()
    buf = None
    while buf != "":
        buf = input("Please type the item name (press Enter to skip): ")
        if buf == "":
            break
        else:
            price = input("Please type the item price: ")
            amount = input("Please tell me how many you are selling: ")
            vending_items[buf] = (amount, price)

    print("Here are the items you informed me about:\n", vending_items)
