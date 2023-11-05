import requests
import json


def grab_json(url):
    return json.loads(requests.get(url).text)


rosterURL = "https://classes.cornell.edu/api/2.0/config/rosters.json"
rosters = grab_json(rosterURL)['data']['rosters']
roster = rosters[-1]['slug']
if "WI" in roster or "SU" in roster:
    roster = rosters[-2]['slug']

subjectsURL = "https://classes.cornell.edu/api/2.0/config/subjects.json?roster=" + roster
subjects = grab_json(subjectsURL)['data']['subjects']

classesJSON = []
count = 0
for s in subjects:
    count += 1
    print(f'Cycle {count}/184')
    # if count > 10:
    #     break
    classURL = "https://classes.cornell.edu/api/2.0/search/classes.json?roster=" + roster + "&subject=" + s['value']
    classesJSON.extend(grab_json(classURL)['data']['classes'])

classes = []
for c in classesJSON:
    try:
        item = {
            'code': c['subject'] + " " + c['catalogNbr'],
            'title': c['titleLong'],
            'time': [],
        }
    except:
        continue
    for e in c['enrollGroups']:
        for s in e['classSections']:
            for m in s['meetings']:
                place = {
                    'time': m['timeStart'],
                    'timeEnd': m['timeEnd'],
                    'days': m['pattern'],
                    'type': s['ssrComponent']
                }
                item['time'].append(place)
    classes.append(item)

# by this line we have a list of classes
import classManage
import mytime
t1 = mytime.stringtoobject('11:00AM')
t2 = mytime.stringtoobject('1:20PM')
days = 'TR'
classes = classManage.condense_day(days, classes)
classes = classManage.condense_time(t1, t2, classes)
# we can shorten the list by day
for each in classes:
    print(each)


