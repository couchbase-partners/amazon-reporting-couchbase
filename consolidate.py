import os
import csv

def run():
    usage={}
    filenames=get_filenames()

    for filename in filenames:
        [hourly, byol, legacy, revenue] = process_file(filename)

        #filenames look like daily_business_usage_by_instance_type_2015-04-02.csv
        date=filename[48:55] + '-1'

        if not date in usage:
            usage[date]={}
            usage[date]['hourly']=0
            usage[date]['byol']=0
            usage[date]['legacy']=0
            usage[date]['revenue']=0

        usage[date]['hourly']+=hourly
        usage[date]['byol']+=byol
        usage[date]['legacy']+=legacy
        usage[date]['revenue']+=revenue

    write_usage(usage)

def get_filenames():
    filenames=[]
    for file in os.listdir("./reports"):
        if file.endswith(".csv"):
            filenames.append(os.path.join("./reports", file))
    return filenames

def process_file(filename):
    hourly=0
    byol=0
    legacy=0
    revenue=0

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'Hourly' in row['Product Title']:
                hourly+=int(row['Usage Units'])
            elif 'BYOL' in row['Product Title']:
                byol+=int(row['Usage Units'])
            else:
                legacy+=int(row['Usage Units'])
            revenue+=float(row['Estimated Revenue'])

    return [hourly, byol, legacy, revenue]

def write_usage(usage):
    print('Month, Hourly Pricing Usage, BYOL Usage, Legacy Usage, Total Usage, Revenue')
    for date in usage:
        total = usage[date]['hourly']+usage[date]['byol']+usage[date]['legacy']
        print(date + ', ' + str(usage[date]['hourly']) + ', ' + str(usage[date]['byol']) + ', ' + str(usage[date]['legacy']) + ', ' + str(total) + ', ' + str(usage[date]['revenue']))

run()
