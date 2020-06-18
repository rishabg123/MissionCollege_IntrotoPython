import math
print("Enter your weight in kgs")
weight = float(input())
print("Enter your height in meters")
height = float(input())
bmi = weight / math.pow(height, 2)
if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9 and bmi >= 18.5:
    print("Normal")
elif bmi <= 29.9 and bmi >= 25:
    print("Normal")
else:
    print("Obese")