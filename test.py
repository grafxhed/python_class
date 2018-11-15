"""x = 1
while True:
    print ("To infinity and beyond! We're getting close, on %d now!" % (x))
    x += 1

variable= value if (statement of test) else (other value)"""

"""for x in range(0, 3):
    print ("We're on time %d" % (x))"""

"""user= input ("type something separated by a comma: ")
test= (user.lower()).split()
if test [0]=="age":
       print("thank you, for telling me your age",)
elif test[0]=="name":
       print("thank you, for telling me your name",test[1])
else:
       print("i don't understand")"""


"""baby_names= open("babies.csv")
for i in range(100):
       baby_names.readline()
       print(i)
       if i == 25:
              x = baby_names.readline()
              print(x)"""

baby_names= open("babies.csv","r")
names_str= baby_names.read()
split_list= names_str.split()
name_list= []
list_length= len(split_list)
for i in range(list_length):
    target_val= split_list[i].split(",")
    name_list.append(target_val[2])
print(name_list)

non_dupli_list=[]
occurencies=[]

length_name_list= len(name_list)
for i in range(length_name_list):
    if name_list[i] in non_dupli_list:
        pass
    elif name_list[i] not in non_dupli_list:
        occurence = name_list.count(name_list[i])
        non_dupli_list.append(name_list[i])
        occurencies.append(occurence)

print(len(non_dupli_list),len(name_list))
for i in range(len(non_dupli_list)):
    print("name: ", non_dupli_list[i], "'\t\toccurence: ", occurencies[i])