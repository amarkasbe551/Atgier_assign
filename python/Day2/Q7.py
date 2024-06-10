# 7. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 2
# Expected Result :246  (2+22+222)
 
n = str(input("Enter Value:-"))
print(int(n)+ int(n * 2) + int(n * 3))