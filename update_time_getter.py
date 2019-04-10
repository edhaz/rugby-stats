import os
import re
import datetime
from dateutil import parser

PATH = 'data_archive/'
FILE_NAMES = sorted([item for item in os.listdir(PATH)])

def update_time_getter():
    date_list = []
    date_regex = re.compile(r'(\d+)-(\d+)-(\d+)')
    for item in FILE_NAMES:
        try:
            found = date_regex.search(item).group()
            date_list.append(found)
        except AttributeError:
            continue
    return parser.parse(date_list[-1])
