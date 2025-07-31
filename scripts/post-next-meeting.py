from icalendar import Calendar
import requests

ics = requests.get('https://www.meetup.com/Oak-Hill-Toastmasters/events/ical/');
calendar = Calendar.from_ical(ics.text)

for event in calendar.walk('VEVENT'):
    status = event.get('STATUS')
    if status == "CONFIRMED":
        url = event.get('URL')
        date = event.get('DTSTART')
        month = date.dt.strftime('%B')
        day = date.dt.day
        year = date.dt.year

        # Now replace the line of HTML for our next meeting link in Meetup

        print(f"  Next confirmed event: {month} {day}, {year}")
        print(f"  url: {url}")
        break


