import os
import csv

def run():
    usage={}
    filenames=get_filenames()

    for filename in filenames:
        [enterprise, community] = process_file(filename)

        #filenames look like daily_business_usage_by_instance_type_2015-04-02.csv
        date=filename[48:55] + '-1'

        if not date in usage:
            usage[date]={}
            usage[date]['enterprise']=0
            usage[date]['community']=0

        usage[date]['enterprise']+=enterprise
        usage[date]['community']+=community

    write_usage(usage)

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

def write_usage(usage):
    print('Date,Enterprise,Community,Total')
    for date in usage:
        total = usage[date]['enterprise']+usage[date]['community']
        print(date + ',' + str(usage[date]['enterprise']) + ',' + str(usage[date]['community']) + ',' + str(total))

run()
