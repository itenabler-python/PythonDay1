

Mickhr = 3.5

Alicehr = 2.5

diffhr = Mickhr - Alicehr
# diffhr = round(diffhr)
print("%d"%diffhr)
print("Difference in hour between Mick & Alice in seconds:" + str(diffhr * 3600) )
print("Difference in %.2f hour between Mick & Alice is %d seconds"%(diffhr, diffhr * 3600) )

print("Mick hr {0:.2f} and Alice hr {1:.1f} , difference is {2:.3f} in seconds"
      .format(Mickhr, Alicehr, diffhr) )