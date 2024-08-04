# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight/(height**2))
basicprint = (f"Your BMI is {BMI}, you ")
if (BMI) < 18.5:
    BMIcode = ("are underweight.")
elif (BMI) < 25:
    BMIcode = ("have a normal weight.")
elif (BMI) < 30:
    BMIcode = ("are slightly overweight.")
elif (BMI) < 35:
    BMIcode = ("are obese.")
else:
    BMIcode = ("are clinically obese.")

print(basicprint + BMIcode)