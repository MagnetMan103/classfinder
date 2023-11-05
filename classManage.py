import mytime


def condense_day(days, classes):
    """
    returns an array of classes with the desired day
    """
    newclasses = []
    for each in classes:
        times = each['time']
        for time in times:
            day = time['days']
            if day == days:
                newclasses.append([each['code'], each['title'], time['time'], time['timeEnd'], time['days'], time['type']])
    return newclasses


def condense_time(time1, time2, classes):
    newclasses = []
    for each in classes:
        stringtime = each[2]
        stringtime2 = each[3]
        try:
            timeobj = mytime.stringtoobject(stringtime)

            timeobj2 = mytime.stringtoobject(stringtime2)
        except:
            continue
        if timeobj.isbetween(time1, time2):
            newclasses.append(each)
    return newclasses
