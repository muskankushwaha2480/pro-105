import csv
import math

with open("data.csv" , newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#sorting the data to get the list
data = file_data[0]

#finding the mean
def mean(data):
    n = len(data)
    total = 0

    for p in data:
        total += int(p)

    mean = total/n
    return mean

#squaring the values
squared_list = []
for number in data :
    x = int(number) - mean(data)
    x = x**2
    squared_list.append(x)

#getting the sum
sum = 0
for y in squared_list:
    sum = sum + y

#dividing the sum by total values
result = sum/(len(data) - 1 )

# getting the deviation by taking the square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)