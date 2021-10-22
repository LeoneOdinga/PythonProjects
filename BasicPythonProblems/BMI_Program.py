# get inputs from users then display their BMI and related interpretation

#prompt for the inputs

weight=float(input("Enter Your Weight: "))
height =float(input("Enter Your Height: "))

#function to calculate the BMI
def calculateBMI(personWeight,personHeight):
    return personWeight/(personHeight*personHeight)

#function to get the BMI interpretation
def interpretBMI():
    comment =" "
    returnedBMI = calculateBMI(weight,height)
    if(returnedBMI<18.5):
        comment="Under-Weight"
    elif  returnedBMI>18.5 and returnedBMI <25:
        comment= "Normal Weight"
    elif returnedBMI >25 and returnedBMI <30:
        comment ="Obese"
    else:
        comment="Clinically obese!"
    return comment

#display the results to the user

print("Your BMI is: ",calculateBMI(weight,height))
print()
print("Interpretation: "+interpretBMI())
