import os
import re
import datetime
from dateutil import parser

def update_time_getter(year):
    PATH = os.path.dirname(os.path.realpath(__file__)) + '/data_archive/' + str(year) + '/'
    FILE_NAMES = sorted([item for item in os.listdir(PATH)])
    date_list = []
    date_regex = re.compile(r'(\d+)-(\d+)-(\d+)')
    for item in FILE_NAMES:
        try:
            found = date_regex.search(item).group()
            date_list.append(found)
        except AttributeError:
            continue
    return parser.parse(date_list[-1])
