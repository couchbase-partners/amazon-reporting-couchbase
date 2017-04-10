import os
import csv

def run():
    filenames=get_filenames()

    for filename in filenames:
        [enterprise, community] = process_file(filename)

        #filenames look like daily_business_usage_by_instance_type_2015-04-02.csv
        s=filename[38:]
        print(s)

def get_filenames():
    filenames=[]
    for file in os.listdir("./reports"):
        if file.endswith(".csv"):
            filenames.append(os.path.join("./reports", file))
    return filenames

def process_file(filename):
    community=0
    enterprise=0

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'Enterprise' in row['Product Title']:
                enterprise+=int(row['Usage Units'])
            else:
                community+=int(row['Usage Units'])

    return [enterprise, community]

run()
