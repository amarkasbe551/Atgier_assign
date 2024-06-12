# 3. Write a Python class to implement pow(x, n) function.

class PowerFunction:
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.pow(x, -n)
        elif n % 2 == 0:
            return self.pow(x * x, n // 2)
        else:
            return x * self.pow(x, n - 1)


# Creating an instance of the PowerFunction class
power_function = PowerFunction()

print(power_function.pow(4, 7))  
print(power_function.pow(7, 10))  
print(power_function.pow(5, -5)) 
