def sum_of_natural_no(n):
    if (n <= 0):
       print("a positive integer")
    return (n * (n+1)) //2

n=int(input("enter the number:"))
result = sum_of_natural_no(n)
print(f"the sum of first {n} natural no is:{result}")

or

n = int(input("enter the number:"))
c = n*n+1 / 2 ;
print("The sum of n natural no is ",c)

