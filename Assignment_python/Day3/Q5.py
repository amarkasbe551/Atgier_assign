# 5. Write a Python program to calculate the number of days between two dates.
# Note: from datetime import date
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

count = date(2014, 7, 11) - date(2014, 7, 2)
print("Answer:-",count)