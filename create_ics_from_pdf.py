from ics import Calendar, Event
from pdfreader import load_table, get_events

c: Calendar = Calendar()


def debug_event():
    eve = Event()
    eve.name = "Sahri Ends"  # ev["title"]
    eve.begin = '2020-04-25T05:29:00+08:00'  # ev["start_time"]
    c.events.add(eve)


# get events from pdfreader module
all_events = get_events()

for ev in all_events:
    e = Event()
    e.name = ev["title"]
    e.begin = ev["start_time"]
    # e.duration = ''
    c.events.add(e)

with open('my_cal.ics', 'w') as f:
    f.write(str(c))
