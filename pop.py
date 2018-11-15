
names= []
structured_list=[]
for x in range(2):
    user_input = input("enter attendance info separated by a comma: ")
    x= user_input
    names.append(x)

print (names)

for user in range(len(names)):
    split = names[user].split(",")
    print (names[user].split(","))
    info= {"name": (split[0]).strip(),
           "name": (split[1]).strip(),
           "name": (split[2]).strip(),
           "time": (split[3]).strip()}
    
    structured_list.append(info)
    
print(structured_list)

while True:
    user_input= input("enter a username to search: ")
    for user in structured_list:
        print(len(user["uname"]),len(user_input))
        if user["user"] ==user_input:
            print(user["uname"],user["lname"],user["name"],user["time"])

        else:
            print("user not found, please try again.")
