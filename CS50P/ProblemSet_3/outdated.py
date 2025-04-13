months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def convert_date(date_str):
    # Try to handle MM/DD/YYYY format first
    try:
        # Split the date string by '/'
        month, day, year = date_str.split('/')
        # Convert to integers to validate the range
        month = int(month)
        day = int(day)
        year = int(year)
        
        # Check if month and day are within valid ranges
        if 1 <= month <= 12 and 1 <= day <= 31:
            # Return the date in ISO 8601 format
            """
            0: If the number has fewer than 4 digits, pad it with leading zeros.
            4: Ensure at least 4 digits are printed.
            d: Format the value as an integer.
            """
            return f"{year:04d}-{month:02d}-{day:02d}"      
    except ValueError:
        pass

    # Handle Month Day, Year format
    try:
        # Split the date string by spaces and comma
        """
        1: This is the maximum number of splits to perform. 
        By specifying 1, the .split() method will only split the string 
        at the first occurrence of the space character
        """
        month_str, day_year_str = date_str.split(' ', 1)
        day_str, year_str = day_year_str.split(', ')
        day = int(day_str)
        year = int(year_str)
        
        # Get the corresponding numeric month value
        if month_str in months and 1 <= day <= 31:
            month = months[month_str]
            # Return the date in ISO 8601 format
            return f"{year:04d}-{month}-{day:02d}"
    except (ValueError, KeyError):
        pass

    # If the date couldn't be parsed, return None
    return None

def main():
    while True:
        # Prompt the user for a date
        date_str = input("Date: ")
        
        # Convert the date
        iso_date = convert_date(date_str)
        
        # If the conversion was successful, print the ISO date and break the loop
        if iso_date:
            print(iso_date)
            break

# Run the program
if __name__ == "__main__":
    main()

