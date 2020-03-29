import csv
import json
import os

#setting up the file path
script_dir = os.path.dirname(__file__)
rel_path = "../data/population.csv"
abs_file_path = os.path.join(script_dir, rel_path)

#this dictionaty will hold the parsed data in JSON format
population_dict=[]

#parsing CSV
with open(abs_file_path, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        population_dict.append([row[0],row[1]])

#writing dictionary to a JSON file
out_file = open('population.json','w+')
json.dump(population_dict, out_file)


