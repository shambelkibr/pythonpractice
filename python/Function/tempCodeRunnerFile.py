def checked_season(month):
    if month > 9:
        return "summer"
    elif month > 6:
        return "spring"
    elif month > 3:
        return "winter"
    else:
        return "autumn"

# Get user input


month = int(input("Enter the month number (1-12): "))

# Call the function and print the result
season = checked_season(month)
print(f"The season is: {season}")