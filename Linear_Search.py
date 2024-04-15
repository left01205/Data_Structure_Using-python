def linear_search(l,t):
  for i in l:
    if (i==t):
      return 1

l=eval(input("Enter data in list format = "))
t=eval(input("Enter target elemet = "))
res= linear_search(l,t)
if res==1:
  print("Target element found")
else:
  print("Target element not found")
