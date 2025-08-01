from icalendar import Calendar
import fileinput
import requests

ics = requests.get('https://www.meetup.com/Oak-Hill-Toastmasters/events/ical/');
calendar = Calendar.from_ical(ics.text)

def replace_next_meeting_line(month, day, year, url):
    print(f"Next meeting: {month} {day}, {year} ({url})")
    file_path = "index.html"
    with fileinput.input(file_path, inplace=True) as file:
        for line in file:
            if "next-meeting-ref" in line:
                num_spaces = len(line) - len(line.lstrip(' '))
                a_tag = f'<a id="next-meeting-ref" href="{url}">Next meeting: {month} {day}, {year}</a>\n'
                print(num_spaces * " " + a_tag, end='')
            else:
                print(line, end='')

for event in calendar.walk('VEVENT'):
    status = event.get('STATUS')
    if status == "CONFIRMED":
        url = event.get('URL')
        date = event.get('DTSTART')
        month = date.dt.strftime('%B')
        day = date.dt.day
        year = date.dt.year

        replace_next_meeting_line(month, day, year, url)
        break


