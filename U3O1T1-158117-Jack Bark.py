
print('hello this is a BMI calculator')


#Used later as equation
def bmi(h, w):
    h = float(h)
    w = float(w)
    bmi = w/(h*h)
    print(bmi)
    #Gives BMI category
    if bmi > 18.5:
        print('You are underweight')
    if 18>bmi<25:
        print('You are a healthy weight')
    if 25<bmi>30:
        print('You are overweight')
    if bmi>30:
        print('You are obese')
    return bmi


#Determines use of imperial or metric
a = input('Are you using imperial(i) or metric(m)? ')
#User input height and weight in either imperial or metric
if a == 'i' or 'I':
        h = input('Please enter your height in feet: ')
        h = h*12
        f = input('Please enter your height in inches:')
        h = float(h+f)
        h = (h*0.0254)
        w = (float(input('Please enter your weight Lbs: ')))
        w = w*0.45359237
        bmi(h, w)
elif a == 'm' or 'M':
        h = input('Please enter your height in meters: ')
        w = input('Please enter you weight in Kg: ')
        bmi(h, w)
if a != 'm' or 'M' or 'i' or 'I':
    print('Do as instructed!')
    exit(1)






