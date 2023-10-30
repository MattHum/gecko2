import requests
import json
import csv
import creds
test_string = {
  "bitcoin": {
    "eur": 26848
  },
  "bitcoin-cash": {
    "eur": 215.97111
  },
  "litecoin": {
    "eur": 58.19911
  }
}


#Daten aus dict zu dict kopieren
#new dict
new_string = {}
for i, j in test_string.items():
  new_string[i] = test_string[i]['eur']

for i, j in new_string.items():
  print(i,';',j)

#order dict
ordered_dict = {}
order_list = ['litecoin', 'bitcoin-cash','bitcoin']
for item in order_list:
  ordered_dict[item] = new_string[item]
#print(ordered_dict)


#csv_columns = ['coin','EUR']
#csv_file = "Names2.csv"
#try:
#with open(csv_file, 'w') as csvfile:
 # writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
  #writer.writeheader()
  #for data in ordered_dict:
  #writer.writerow(data)
#except IOError:
 # print("I/O error")

#funktioniert Option 1
#with open('my_file.csv', 'w', newline='') as f:
 #  writer = csv.DictWriter(f, fieldnames=ordered_dict.keys())
  # writer.writeheader()
   #writer.writerow(ordered_dict)
   

#funktioniert Option 2
# Open the CSV file with write permission
#with open("output.csv", "w", newline="") as csvfile:
    # Create a CSV writer using the field/column names
 #   writer = csv.DictWriter(csvfile, fieldnames=order_list)

    # Write the header row (column names)
  #  writer.writeheader()
   # writer.writerow(ordered_dict)

# Option 3
# Create a dictionary of key-value pairs
#data = {'A':42, 'B':41, 'C':40}
# Open the file in writing mode (no blank lines)
#with open('my_file2.csv', 'w', newline='') as f:
 #   # Create a CSV writer object
  #  writer = csv.writer(f)
   # # Write one key-value tuple per row
    #for row in ordered_dict.items():
     #   writer.writerow(row)

# Option 4 -> funktioniert!
#with open('my_file3.csv', 'w') as f:
 #   for key, value in ordered_dict.items():
  #      f.write(f'{key};{value}\n')

# change point to comma

print(type(ordered_dict['bitcoin']))


#for k in ordered_dict:
 #   if type(ordered_dict[k]) == '.' in ordered_dict[k]:
  #    ordered_dict[k] = float(ordered_dict[k].replace('.',','))
#print(ordered_dict)

for i, j in ordered_dict.items():
  test = f'{ordered_dict[i]:.2f}' #convert float/int to string 
  ordered_dict[i] = test.replace('.', ',') #replace point with comma
print(ordered_dict)


ac = creds.ab
print(ac)