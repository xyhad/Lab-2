def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Weight classification - Under Weight")
    elif bmi<=25.0 and bmi>=18.5:
        print("Weight classification - Normal weight")
    elif bmi > 25.0:
        print("Weight classification - Over Weight")


calculate_bmi(weight=57, height=1.73)
