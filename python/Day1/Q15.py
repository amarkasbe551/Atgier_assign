# Take input of distance between two cities in Km convert this value in meters, feet, inches and centimeters
# Input distance between two cities in kilometers

distance_km = float(input("Enter the distance between two cities in kilometers: "))


print(f"Distance in meters:-{distance_km * 1000} m")
print(f"Distance in feet:-{distance_km * 3280.84} ft")
print(f"Distance in feet:-{distance_km * 39370.1} in")
print(f"Distance in feet:-{distance_km * 100000} cm")


