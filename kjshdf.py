import math

a = int(input("enter 'a' value : "))
b = int(input("enter 'b' value : "))

a_2 = pow(a , 2)
b_2 = pow(b , 2)

final_result = a_2 + b_2
c = math.sqrt(final_result)

print(c)