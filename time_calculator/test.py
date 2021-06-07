days = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
        4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}


def _time24to12(time: str):

    h, m = time.split(":")
    h = int(h)
    m = int(m)
    if h < 12 and h != 0:
        return "%s:%s AM" % (format_m(h), format_m(m))
    if h == 12:
        return "12:%s AM" % (format_m(m))

    if h == 0:

        return "12:%s PM" % (format_m(m))
    if h > 12:

        return "%s:%s PM" % (format_m(h-(h//12)*12), format_m(m))


def _time12to24(time: str, pmam):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    if pmam == "PM":
        if h == 12:
            return "00:%s" % (format_m(m))

        else:

            return "%s:%s" % (format_m(h+12), format_m(m))

    if pmam == "AM":
        return "%s:%s" % (format_m(h), format_m(m))


def format_m(i: int):
    if i < 10:
        return "0"+str(i)
    else:
        return str(i)


def anyTimeTo24(time: str, withdate: bool = False):
    # "2205:12" =
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    nbhours = h-(h//24)*24
    nbdays = (h//24)
    if withdate:
        return "%s:%s %s" % (format_m(nbhours), format_m(m), str(nbdays))

    else:
        return "%s:%s" % (format_m(nbhours), format_m(m))


def _addTwoTime24(time1: str, time2: str, withdate=False):
    h1, m1 = time1.split(":")
    h1 = int(h1)
    m1 = int(m1)
    h2, m2 = time2.split(":")
    h2 = int(h2)
    m2 = int(m2)
    s = "%s:%s" % (format_m(h1+h2+((m1+m2)//60)),
                   format_m((m1+m2)-((m1+m2)//60)*60))

    return anyTimeTo24(s, withdate=withdate)


def normalizeDate(date: str, deca: int = None):
    date = date.lower()[:3]
    normalizedd = ""

    for j in days:
        if days[j].lower()[:3] == date:
            if deca:
                normalizedd = days[(j+deca)-((j+deca)//7)*7]
            else:
                normalizedd = days[j]

    return normalizedd


def add_time(start, duration, _date: str = None):
    myTime24 = _time12to24(start.split(' ')[0], start.split(' ')[1])
    timeToAdd24, _ = anyTimeTo24(duration, withdate=True).split(" ")
    myDay = ""

    new_time, _days = _addTwoTime24(myTime24, timeToAdd24, True).split(" ")
    _days = int(_days)+int(_)
    print("..............",(7+_days)-((7+_days)//7)*7)
    if _date:
        myDay = normalizeDate(_date)
        if _days == 0:
            return "%s, %s" % (_time24to12(new_time), myDay)
        if _days == 1:
            return "%s (next day)" % (_time24to12(new_time))
        else:
            return "%s, %s (%d days later)" % (_time24to12(new_time), myDay, _days)
    else:
        if _days == 0:
            return "%s" % (_time24to12(new_time))
        if _days == 1:
            return "%s (next day)" % (_time24to12(new_time))
        else:
            return "%s (%d days later)" % (_time24to12(new_time), _days)


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12","Friday"))
# Returns: 7:42 AM (9 days later)
