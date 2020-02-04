import csv

with open('inventory.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_idx = 0
    for row in csv_reader:
        if line_idx == 0:
            print('Skipping header.')
        else:
            print(f'Datacentre: {row[0]} device name {row[7]}')
        line_idx += 1
