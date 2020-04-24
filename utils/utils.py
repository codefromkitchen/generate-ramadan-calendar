from datetime import *


def format_time(twelve_hour_time):
    m2 = '1:35 PM'
    m2 = datetime.strptime(m2, '%I:%M %p')
    print(str(m2).split(" ")[1])

