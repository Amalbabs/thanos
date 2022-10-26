import math
s1=int(input ("side1:"))
s2=int(input ("side2:"))
s3=int(input ("side3;"))
s=(s1+s2+s3)/2
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("area of triangle:",area)              