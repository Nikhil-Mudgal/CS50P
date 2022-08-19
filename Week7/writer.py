import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("writer_text.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"home":home,"name":name})