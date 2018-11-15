# Simple programme to add two fractions and give answer as fraction 
def add(a,b):
        sum = a+b
        return sum

def times(a,b):
        '''This function multiplies two arguments'''
        multiple = a*b
        return multiple

def divide(a,b):
        divide = a/b
        return divide

def frac_man(num1, num2, den1, den2):
        '''this guy adds two fractions together '''
        full_den = times(den1,den2)
        up1 = times(divide(full_den,den1),num1)
        up2 = (full_den/den2)*num2
        full_num = up1 + up2
        return [full_num, full_den]

def print_man(num1, num2, den1, den2,result):
        print ("\nAnswer = ", result[0], "/", result[1])
        print("\n", num1, "/", den1, "+", num2, "/", den2, "is ---> ", result[0], "/", result[1])

num1 = int(input ("Enter Numerator 1 :"))
den1 = int(input ("Enter Denominator 1 :"))
num2 = int(input ("Enter Numerator 2 : "))
den2 = int(input ("Enter Denominator 2 :"))

result = frac_man(num1, num2, den1, den2)
print_man(num1, num2, den1, den2,result)