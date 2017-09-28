import os
import csv

usage={}

def run():
    filenames=get_filenames()
    for filename in filenames:
        process_file(filename)
    write_usage(usage)

def get_filenames():
    filenames=[]
    for file in os.listdir("./reports"):
        if file.endswith(".csv"):
            filenames.append(os.path.join("./reports", file))
    return filenames

def process_file(filename):
    #filenames look like daily_business_usage_by_instance_type_2015-04-02.csv
    date=filename[48:55] + '-1'

    if not date in usage:
        usage[date]={}
        usage[date]['hourly']=0
        usage[date]['byol']=0
        usage[date]['legacyfree']=0
        usage[date]['legacypaid']=0
        usage[date]['revenue']=0
        usage[date]['legacyrevenue']=0

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if 'Hourly' in row['Product Title']:
                usage[date]['hourly']+=int(row['Usage Units'])
                usage[date]['revenue']+=float(row['Estimated Revenue'])
            elif 'BYOL' in row['Product Title']:
                usage[date]['byol']+=int(row['Usage Units'])
                usage[date]['revenue']+=float(row['Estimated Revenue'])
            elif float(row['Estimated Revenue'])==0:
                usage[date]['legacyfree']+=int(row['Usage Units'])
            else:
                usage[date]['legacypaid']+=int(row['Usage Units'])
                usage[date]['legacyrevenue']+=float(row['Estimated Revenue'])

def write_usage(usage):
    print('Month, Hourly Pricing Usage, BYOL Usage, Legacy Paid Usage, Legacy Free Usage, Total Usage, Revenue, Legacy Revenue, Total Revenue')
    for date in usage:
        totalusage = usage[date]['hourly'] + usage[date]['byol'] + usage[date]['legacypaid'] + usage[date]['legacyfree']
        totalrevenue = usage[date]['revenue'] + usage[date]['legacyrevenue']
        print(
            date + ', '
            + str(usage[date]['hourly']) + ', '
            + str(usage[date]['byol']) + ', '
            + str(usage[date]['legacypaid'])+ ', '
            + str(usage[date]['legacyfree']) + ', '
            + str(totalusage) + ', '
            + str(usage[date]['revenue']) + ', '
            + str(usage[date]['legacyrevenue']) + ', '
            + str(totalrevenue))

run()
