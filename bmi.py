Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your weight in kilograms:"))
Height= Height/100
BMI= Weight/(Height*Height)
print("Your body mass index is: ",BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are severely underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("You are normal weight")
    elif(BMI<=30):
        print("You are overweight")
    else: print("You are severely overweight")
else:("Enter valid details")