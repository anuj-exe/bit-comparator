a0 =bool(1)
a1 =bool(0)
a2 =bool(0)
a3 =bool(1)
s0 =bool(0)
#a binary number is positive 1001 (a3 a2 a1 a0)

b0 =bool(0)
b1 =bool(1)
b2 =bool(0)
b3 =bool(1)
s1 =bool(1)
#b binary number is negative 1010 (b3 b2 b1 b0) 

t1 = (a0,a1,a2,a3,s0)
t2 = (a0,a1,a2,a3,s1)

w = a0 or a1 or a2 or a3 or b0 or b1 or b2 or b3 
x = ((not(a3^b3)) and (not(a2^b2)) and (not(a1^b1)) and (not(a0^b0)))
y = ((b3 and (not a3)) or ((not (a3^b3)) and (b2 and (not a2))) or ((not(a3^b3)) and (not(a2^b2)) and (b1 and (not a1))) or ((not(a3^b3)) and (not(a2^b2)) and (not(a1^b1))  and (b0 and (not a0))))
z=((a3 and (not b3)) or ((not (a3^b3)) and (a2 and (not b2))) or ((not(a3^b3)) and (not(a2^b2)) and (a1 and (not b1))) or ((not(a3^b3)) and (not(a2^b2)) and (not(a1^b1))  and (a0 and (not b0))))

if (s1 and (not s0)):
    if z or x or y:
        print(True)
elif (not w):
    print (True)
elif (s0 and (not s1)):
    if z or x:
        print (False)
    if y:
        print(True) 
elif (s1 and s0):
    if y or x:
        print(True)
    if z:
        print(False)
elif (not (s1 or s0)):
    if x or z:
        print(True)
    if y:
        print(False)  
else:
    print(False)
