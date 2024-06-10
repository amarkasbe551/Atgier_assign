import sympy
import time
import psutil

def count_primes(Num):
    prime_count = 0
    for num in range(1, Num + 1):
        if sympy.isprime(num):
            prime_count += 1
    return prime_count

num = int(input("Enter Number: "))
start_time = time.time()
prime_count = count_primes(num)
end_time = time.time()
execution_time = end_time - start_time
# Get memory usage in bytes
memory_usage_bytes = psutil.Process().memory_info().rss
memory_usage_kb = memory_usage_bytes / 1024
print(f"Memory usage: {memory_usage_kb} kilobytes")
print(f"Number of prime numbers: {prime_count}")
print(f"Execution Time: {execution_time} seconds")
