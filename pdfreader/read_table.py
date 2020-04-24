import tabula
from config import *

table_from_pdf = {}
all_events = {}


# todo: @kazilamisa
def load_table():
    global table_from_pdf
    # takes some time (3-4 sec), consider adding as a startup/on_load script
    table_from_pdf = tabula.read_pdf(INPUT_FILE_PATH, pages='all')

    # table_from_pdf[0] contains whole table, separated by " " (whitespace)
    print(table_from_pdf[0])

    """
          رمضان IMSAK SUBUH SYURUK ZOHOR  ASAR MAGHRIB ISYAK April 2020
    0   هـ 1441   NaN   NaN    NaN   NaN   NaN     NaN   NaN        NaN
    1         1  5 30  5 40   6 59  1 04  4 22    7 09  8 19  24/4/2020
    2         2  5 29  5 39   6 58  1 04  4 22    7 09  8 19  25/4/2020
    3         3  5 29  5 39   6 58  1 04  4 22    7 09  8 18  26/4/2020
    4         4  5 29  5 39   6 58  1 04  4 22    7 08  8 18  27/4/2020
    5         5  5 28  5 38   6 58  1 04  4 22    7 08  8 18  28/4/2020
    6         6  5 28  5 38   6 58  1 04  4 22    7 08  8 18  29/4/2020
    7         7  5 28  5 38   6 57  1 03  4 23    7 08  8 19  30/4/2020
    8       NaN   NaN   NaN    NaN   NaN   NaN     NaN   NaN        May
    9       NaN   NaN   NaN    NaN   NaN   NaN     NaN   NaN       2020
    10        8  5 28  5 38   6 57  1 03  4 23    7 08  8 19   1/5/2020
    11        9  5 27  5 37   6 57  1 03  4 23    7 08  8 19   2/5/2020
    12       10  5 27  5 37   6 57  1 03  4 23    7 08  8 19   3/5/2020
    13       11  5 27  5 37   6 57  1 03  4 23    7 08  8 19   4/5/2020
    14       12  5 27  5 37   6 57  1 03  4 23    7 08  8 19   5/5/2020
    15       13  5 26  5 36   6 57  1 03  4 24    7 08  8 19   6/5/2020
    16       14  5 26  5 36   6 57  1 03  4 24    7 08  8 19   7/5/2020
    17       15  5 26  5 36   6 57  1 03  4 24    7 08  8 19   8/5/2020
    18       16  5 26  5 36   6 57  1 03  4 24    7 08  8 19   9/5/2020
    19       17  5 26  5 36   6 56  1 03  4 24    7 08  8 19  10/5/2020
    20       18  5 25  5 35   6 56  1 03  4 24    7 08  8 19  11/5/2020
    21       19  5 25  5 35   6 56  1 03  4 25    7 08  8 19  12/5/2020
    22       20  5 25  5 35   6 56  1 03  4 25    7 08  8 20  13/5/2020
    23       21  5 25  5 35   6 56  1 03  4 25    7 08  8 20  14/5/2020
    24       22  5 25  5 35   6 56  1 03  4 25    7 08  8 20  15/5/2020
    25       23  5 25  5 35   6 56  1 03  4 25    7 08  8 20  16/5/2020
    26       24  5 25  5 35   6 56  1 03  4 26    7 08  8 20  17/5/2020
    27       25  5 24  5 34   6 56  1 03  4 26    7 08  8 20  18/5/2020
    28       26  5 24  5 34   6 56  1 03  4 26    7 08  8 21  19/5/2020
    29       27  5 24  5 34   6 56  1 03  4 26    7 08  8 21  20/5/2020
    30       28  5 24  5 34   6 56  1 03  4 26    7 08  8 21  21/5/2020
    31       29  5 24  5 34   6 57  1 03  4 27    7 08  8 21  22/5/2020
    32       30  5 24  5 34   6 57  1 03  4 27    7 08  8 21  23/5/2020
    """
    return table_from_pdf[0]  # or just return the columns necessary


# todo: @kazilamisa
# returns a dict of events { date, time, title } to be added as a calendar
def get_events():
    # todo: process 12 hour time to 24 hour time here

    # todo: process utc time here
    # UTC_TIME_DELTA etc.

    # return start_time, title here
    return all_events
