a,b,c,d=map(int,input().split(" "))
tv1=a-a*c/100
tv2=b-b*d/100
if tv1<tv2:
    print("first")
elif tv1>tv2:
    print("second")
else:
    print("Any")
      
