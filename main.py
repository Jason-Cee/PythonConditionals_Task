# New Speed demerit system
Your_average_speed_in_km_per_hr = int(input("Enter your average speed in km/h: "))
The_legal_road_speed_limit = int(input("Enter the allowed speed limit "))

# make the points increase if we need it to
Points = 0
if Your_average_speed_in_km_per_hr < The_legal_road_speed_limit:
    print("OK")
else:
    while Your_average_speed_in_km_per_hr > The_legal_road_speed_limit:
        Your_average_speed_in_km_per_hr -= 5
        Points += 1
    print("Points: " + str(Points))
    if Points > 12:
        print("Time to go to jail")
