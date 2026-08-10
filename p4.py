#we practice +/-/0 , odd/even, student's grade, greatest among 3, 

print("Please enter three values below:- ")

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))

if n1 >= n2 and n1 >= n3:
    print(f"n1 ({n1}) is the greatest")
elif n2 >= n1 and n2 >= n3:
    print(f"n2 ({n2}) is the greatest")
else:
    print(f"n3 ({n3}) is the greatest")

