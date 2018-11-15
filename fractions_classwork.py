"""num1= int(input("what is the numerator 1: "))
den1= int(input ("what is the denominator 1: "))
num2= int(input("what is the numerator 2: "))
den2= int(input ("what is the denominator 2: "))
num3= int(input("what is the numerator 3: "))
den3= int(input ("what is the denominator 3: "))
num4= int(input("what is the numerator 4: "))
den4= int(input ("what is the denominator 4: "))

total_den= (den1 +den2+den3+den4)

up1= int(total_den/den1)*num1
up2= int(total_den/den2)*num2
up3= int(total_den/den3)*num3
up4= int(total_den/den4)*num4

total_num= up1+up2+up3+up4

answer= (total_num / total_den)
print(total_num,"/",total_den)
print(num1,"/",den1,"+", num2,"/",den2,"+", num3,"/",den3,"+", num4,"/",den4,"=", total_num, "/", total_den)
print("answer is: ", total_num/total_den)
"""
import math
print("\nPythagoras calculator app v.0.1\n")
#user_input = input("\twhat value do you want to find?: ")
print("\n\tFrom the formula, c**2 = a**2 + b**2")
while True:
    user_input = input("\n\twhat value do you want to find? a) b) or c): ")  
    if user_input == "c":
        a = float(input("\twhat is the value of 'a'?: "))
        b = float(input("\twhat is the value of 'b'?: "))
        
        print ("\n\tc**2 = a**2 + b**2")
        c=a**2+b**2
        print("\tthe value of c**2 = ",math.sqrt(c),"\n")
    
        
    elif user_input == "a":
        c = float(input("\twhat is the value of 'c'?: "))
        b = float(input("\twhat is the value of 'b'?: "))
        
        print ("\n\ta**2 = c**2 - b**2")
        a=c**2-b**2
        print("\tthe value of a = ",a**2)
            
       
    elif user_input == "b":
        a = float(input("\twhat is the value of 'a'?: "))
        c = float(input("\twhat is the value of 'c'?: "))
        
        print ("\n\tb**2 = c**2 - a**2")
        b=c**2-a**2
        print("\tthe value of b = ",b**2)


    elif user_input == "d":
         break




        
