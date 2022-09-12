a = 57.2  #10, 30
b = 29  #20, 10
c= 8008
d= 835

#simple formula to swap values between two var
a = a + b
b = a - b
a = a - b

c,d,a = a,c,d #This works right to left meaning 
                        # C LHS -> gets the value of A RHS
                        # D LHS -> gets the value of C RHS
                        # A LHS -> gets the value of D RHS


print(a) #835
print(b) #57.2
print(c) #29.0
print(d) #8008

a,b,c,d = d,c,b,a 

print(a) #8008
print(b) #29.0
print(c) #57.2
print(d) #835