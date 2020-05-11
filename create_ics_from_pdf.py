from ics import Calendar, Event
from pdfreader import *
c: Calendar = Calendar()


def debug_event():
    eve = Event()
    eve.name = "Sahri Ends"  # ev["title"]
    eve.begin = '2020-04-25T05:29:00+08:00'  # ev["start_time"]
    c.events.add(eve)


# get events from pdfreader module
all_events = get_events()

for keys in all_events.keys():
    for values in all_events[keys]:
        e = Event()
        e.name = keys
        e.begin = values # ev["start_time"]
        e.location = 'Singapore'
        e.end = values
        c.events.add(e)

with open('my_cal.ics', 'w') as f:
    f.write(str(c))
