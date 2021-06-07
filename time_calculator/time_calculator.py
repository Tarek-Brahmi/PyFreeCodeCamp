def add_time(start=None, duration=None, _date: str = None):
    days = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
        4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}


    def format_m(i: int):
        if i < 10:
            return "0"+str(i)
        else:
            return str(i)


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
        x = list(days.values())
        for j in range(len(x)):
            if x[j].lower()[:3] == date:
                if deca:
                    normalizedd = x[(j+deca)-((j+deca)//7)*7]
                else:
                    normalizedd = x[j]

        return normalizedd


    def reformatTime(time: str, pmam: str, timeToReformat: str, m_start):

        time24 = int(time.split(":")[0])
        _time12 = (time24-(time24//24)*24)

        def _repace(text, _pmam):
            if "PM" in text:
                return text.replace("PM", _pmam)
            if "AM" in text:
                return text.replace("AM", _pmam)

        if _time12 >= 12:
            new_time12 = _time12-12
            if new_time12 > 0:
                if pmam == "AM":
                    return _repace(timeToReformat, "PM")
                if pmam == "PM":
                    return _repace(timeToReformat, "AM")

            if new_time12 == 0:
                if int(time.split(":")[1]) > 0:
                    if pmam == "AM":
                        return _repace(timeToReformat, "PM")
                    if pmam == "PM":
                        return _repace(timeToReformat, "AM")
                else:
                    if pmam == "AM":
                        return _repace(timeToReformat, "PM")
                    if pmam == "PM":
                        return _repace(timeToReformat, "AM")
        else:
            if pmam == "AM":
                return _repace(timeToReformat, "AM")
            if pmam == "PM":
                return _repace(timeToReformat, "PM")



    if not start or not duration:
        raise ValueError("duration and start date are required")
    if not (isinstance(start, str) or isinstance(duration, str)):
        raise TypeError("duration and start must be strings")
    dh, dm = 0, 0
    h, m = 0, 0
    pmam = ""

    try:

        (dh, dm) = duration.split(':')
        if(int(dm) >= 60):
            raise ValueError("minutes must be <60")
    except Exception as ee:
        raise ValueError('duration must hours:minutes')
    try:
        dat = start.split()
        try:
            (h, m) = dat[0].split(':')
            if(int(m) >= 60):
                raise ValueError("minutes must be <60")

        except Exception as ee:
            raise ValueError("make shure : is separate hours and menutes h:m")

    except Exception as e:
        raise ValueError("format off start hour:minute PM/AM")

    myTime24 = _time12to24(start.split(' ')[0], start.split(' ')[1])
    # print("My time to 24 %s" % myTime24)
    timeToAdd24, _ = anyTimeTo24(duration, withdate=True).split(" ")
    # print("time to add to %s is %s" % (myTime24, timeToAdd24))
    myDay = ""
    new_time, _days = _addTwoTime24(myTime24, timeToAdd24, True).split(" ")

    # print('the final time is %s' % _time24to12(new_time))
    _days = int(_days)+int(_)
    if _date:
        myDay = normalizeDate(_date, _days)
        if _days == 0:
            return "%s, %s" % (reformatTime(duration, start.split(' ')[1], _time24to12(new_time), m_start=m), myDay)
        if _days == 1:
            return "%s (next day)" % (reformatTime(duration, start.split(' ')[1], _time24to12(new_time), m_start=m))
        else:
            return "%s, %s (%d days later)" % (reformatTime(duration, start.split(' ')[1], _time24to12(new_time), m_start=m), myDay, _days)
    else:
        if _days == 0:
            return "%s" % (reformatTime(duration, start.split(' ')[1], _time24to12(new_time), m_start=m))
        if _days == 1:
            return "%s (next day)" % (reformatTime(duration, start.split(' ')[1], _time24to12(new_time), m_start=m))
        else:
            return "%s (%d days later)" % (reformatTime(duration, start.split(' ')[1], _time24to12(new_time), m_start=m), _days)


