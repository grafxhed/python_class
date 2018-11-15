# def adder(upperlim,increment,initial):
#     print("initial before increment ==> ",initial)
#     print("upperlim before increment ==> ", upperlim)
#     initial+= increment
#
#     if initial >= upperlim:
#         return initial
#     elif initial<=upperlim:
#         adder(upperlim,increment,initial)
#
#
# print(addeer(50,2,25))
#
# def show_fact(num):
#     val = str(num)
#     for i in reversed(range(1,num)):
#         val += '*'+ str(i)
#     print(val)
#
# def fact()


def sub(a,b,action):
    if action =="s":
        return a - b
    else:
        return "\n\tsorry. not my function"


print(sub(3,4,"d"))