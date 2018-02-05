weight=input("What is your weight in pounds? ")
height=input("What is your height in inches? ")
bmi=703*((int(weight))/(int(height)**2))

print("Your BMI is "+str(bmi))

if (int(bmi) <= 18):
	print("You are underweight.")
elif (int(bmi) >= 18 and int(bmi) <=26):
	print("You are normal weight.")
else:
	print("You are overweight.")
	