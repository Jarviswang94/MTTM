import csv
csv_reader = csv.reader(open("./labeled_data.csv"))
count = 0
count2 = 0
count_all = 0
for line in csv_reader:
	count_all += 1
	sent = line[-1]
	label = line[-2]
	if label == '1':
		count += 1
	if label == '2':
		count2 += 1
print(count)
print(count2)
print(count_all)