'''
Write a CSV-to-JSON translator that expects the path to a CSV file as argument, 
and for each line in the file, prints out a JSON object encapsulating that record 
'''


import csv, sys, json

files = sys.argv[1:]   # place all arguments as files into a variable

# for file in files:
#     with open(file, 'r', encoding='utf-8-sig') as handle:
#         csv_file = csv.DictReader(handle)
#         for row in csv_file:
#             print(json.dumps(row))


# run through each file in argument
for file in files:

    # create a generator for each file
    def iterate_file(file):
        with open(file, 'r', encoding='utf-8-sig') as handle:  # open file and ignore the serialization encoding at each csv file with -sig
            csv_file = csv.DictReader(handle)  # read csv into a dictionary
            for row in csv_file:
                yield json.dumps(row)

    [print(iterate) for iterate in iterate_file(file)]  # call generator
