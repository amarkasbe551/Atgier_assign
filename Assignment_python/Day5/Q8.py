# 8. Write a function for checking the speed of drivers. This function should have one parameter: speed.
# 1.    If the speed is less than 70, it should print “Ok”.
# 2.    Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, (if the speed is 80, it should print: “Points: 2”.)
# 3.    If the driver gets more than 12 points, the function should print: “License suspended”

def ip():
    speed = int(input("Enter Speed: "))
    check(speed)

def check(speed):
    if speed <= 70:
        print("Ok")
    else:
        demerit_points = (speed - 70) // 5
        if demerit_points > 12:
            print("License suspended")
        else:
            print(f"Points: {demerit_points}")

ip()
