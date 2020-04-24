from ics import Calendar, Event
from pdfreader import load_table, get_events

# start loading pdf
load_table()

c: Calendar = Calendar()
e = Event()

# get events from pdfreader module
all_events = get_events()

for e in all_events:
    e.name = "Sahri Ends"  # e["title"]
    e.begin = '2020-04-25T05:43:45+08:00'  # e["start_time"]
    c.events.add(e)

with open('my_cal.ics', 'w') as f:
    f.write(str(c))
