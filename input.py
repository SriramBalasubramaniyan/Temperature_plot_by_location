def user_input():
    try:
         #get latitude, longitude input from user and convert to float
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))
        days = int(input("Enter number of past days (up to 90): ")) #get number of past days input from user and convert to int
        if days < 1 or days > 90: #check if days is within valid range
            print("Days must be between 1 and 90") #print error message if days is not within valid range
            raise ValueError("Days must be between 1 and 90") #raise value error if days is not within valid range
    except ValueError as ve: #catch value error exceptions and store in variable ve
        print(f"Invalid input: {ve}") #print error message for invalid input
        return None, None, None #return None values for latitude, longitude, and days if there is an error
    else:
        print(f"Latitude: {latitude}, Longitude: {longitude}, Days: {days}") #print the valid latitude, longitude, and days values
        return latitude, longitude, days #return the valid latitude, longitude, and days values if there are no exceptions