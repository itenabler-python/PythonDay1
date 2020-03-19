def calcBMI(height,weight):
    # bmi calculation
    height = height / 100  # height in metres
    BMIvalue = weight / (height ** 2)
    return BMIvalue
def BMIstatus(BMIvalue):
    if BMIvalue < 18:
        status = "Underweight"
    elif BMIvalue < 25:
        status = "Ideal"
    elif BMIvalue < 30:
        status = "Overweight"
    else:
        status = "Obese"
    return status
name = input("Please enter your full name:")
myheight = float(input("Please enter height(cm):"))
myweight = float(input("Please enter weight(kg):"))
BMIvalue = calcBMI(myheight, myweight)
mystatus = BMIstatus(BMIvalue)
print("Mr. {0:s} your BMI value is {1:.2f}, {2:s}".format(name, BMIvalue, mystatus))
