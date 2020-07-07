import random
a_file = open("numbers.txt", "r")
numbers = []
ideal = []

for i in range(100):
    for i in range(10):
        a_file.write(str(random.randint(1, 10)))

for i in range(1, 99):
    ideal.append(i)
string_without_line_breaks = ""
for line in a_file:
  stripped_line = line.rstrip()
  string_without_line_breaks += stripped_line
a_file.close()
for i in string_without_line_breaks:
    numbers.append(float(i))

result =  all(elem in numbers  for elem in ideal)
if result == True:
    print("Yes all the numbers are there")
else:
    print("No all the numbers are not there")
