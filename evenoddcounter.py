
try:
    k = 5/ 0
except Exception as e:
    print("Error encounter!")


i = range(1,11)
list2 = [3,4,7,10,11,19,14,15,16,200,231]
evencounter=0
oddcounter=0
for counter in list2:
    if counter % 2 ==0:
        evencounter += 1
    else:
        oddcounter +=1

print("Even counter:{} Odd counter:{}".format(evencounter, oddcounter))

