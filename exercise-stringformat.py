
I = "admin@$E*G$#R@/users/root"

list1 = I.split("@")
print(list1)

for item in list1:
    print(item)

print("number of objects:" + str(len(list1)) )
print("where is admin now " + str(list1.index('admin')))