#!/usr/bin/env python2
# coding: utf-8

import calendar
import datetime
import time

formats = {
    'default': '%a, %d %b %Y %H:%M:%S UTC',

    'iso': '%Y-%m-%dT%H:%M:%S.000Z',

    'utc': '%a, %d %b %Y %H:%M:%S UTC',
    'archive': '%Y%m%d-%H',
    'compact': '%Y%m%d-%H%M%S',
    'daily': '%Y-%m-%d',

    'mysql': '%Y-%m-%d %H:%M:%S',

    'nginxaccesslog': "%d/%b/%Y:%H:%M:%S",
    'nginxerrorlog': "%Y/%m/%d %H:%M:%S",
}


def parse(time_str, fmt_key):
    return datetime.datetime.strptime(time_str, formats[fmt_key])


def format(dt, fmt_key):
    return dt.strftime(formats[fmt_key])


def format_ts(ts, fmt_key):
    dt = ts_to_datetime(ts)
    return format(dt, fmt_key)


def utc_datetime_to_ts(dt):
    return calendar.timegm(dt.timetuple())


def ts_to_datetime(ts):
    return datetime.datetime.utcfromtimestamp(ts)


def ts():
    return int(time.time())


def ms():
    return int(time.time() * 1000)


def us():
    return int(time.time() * (1000 ** 2))


def ns():
    return int(time.time() * (1000 ** 3))


def ms_to_ts(ms):
    return ms / 1000


def us_to_ts(us):
    return us / (1000 ** 2)


def ns_to_ts(ns):
    return ns / (1000 ** 3)


def to_ts(v):
    """
    convert millisecond, microsecond or nanosecond to second
    """

    if (type(v) not in (type(1), type(1L), type(0.1))
            or v < 0):
        raise ValueError('invalid time to convert to second: {v}'.format(v=v))

    l = len(str(int(v)))

    if l == 10:
        return int(v)
    elif l == 13:
        return int(v / 1000)
    elif l == 16:
        return int(v / (1000**2))
    elif l == 19:
        return int(v / (1000**3))
    else:
        raise ValueError(
            'invalid time length, not 10, 13, 16 or 19: {v}'.format(v=v))
