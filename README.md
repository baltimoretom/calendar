Holiday Calendar Generator

This Python script generates an iCalendar file (.ics) containing a holiday and office schedule for the year 2024. It utilizes the icalendar library to create events for holidays, in-office days, and remote working days.

Features

Automatically generates holiday events based on predefined dates.
Determines the "In Office" day for each month.
Creates events for working days, marking them as "In Office" or "Remote."
Outputs the calendar data to an .ics file named lb_calendar.ics.
Requirements

Python 3.x
icalendar library (you can install it via pip with pip install icalendar)
pytz library (you can install it via pip with pip install pytz)
Usage

Make sure you have Python and the required libraries installed.
Execute the script to generate the calendar data.
The resulting calendar file, lb_calendar.ics, will contain the holiday and work schedule for 2024.
Customization

You can customize the script by updating the holidays dictionary or modifying the logic for determining in-office days to fit your specific needs.

License

This script is open-source and available under the MIT License. Feel free to modify and use it according to your requirements.
