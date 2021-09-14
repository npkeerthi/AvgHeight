
h=input("Type all heights of your friends:").split()
summ=0
lent=0
for i in range(0,len(h)):
  new=int(h[i])
  summ+=new
  lent+=1
print("The average height in your friend list is",round(summ/lent))
