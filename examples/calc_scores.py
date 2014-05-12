import csv

f = open('test_scores.csv')
csvfile = csv.reader(f)

def average(lst):
    l = float(len(lst))
    return sum(lst)/l


males = []
females = []

header = csvfile.next() # throw out first row

for row in csvfile:
	sex = row[1]
	score = int(row[3])
    if sex == 'F':
        females.append(score)
    else:
        males.append(score)
print 'Female:', average(females)
print 'Male:', average(males)
f.close()

