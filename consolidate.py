import os
import csv

def run():
    filenames=get_filenames()

    for filename in filenames:
        process_file(filename)

def get_filenames():
    filenames=[]
    for file in os.listdir("./reports"):
        if file.endswith(".csv"):
            filenames.append(os.path.join("./reports", file))
    return filenames

def process_file(filename):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)

run()
