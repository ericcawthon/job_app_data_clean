import datetime

def calc_interviewers_met(endstate):
    if not isinstance(endstate, str):
        return None

    if endstate == "":
        return None
    
    if ("(" in endstate):
        eslist = endstate.split('(')
        return int(eslist[1][:len(eslist)-1])
    else:
        return 0

def clean_end_state(endstate):
    if not isinstance(endstate, str):
        return "Pending"

    if endstate == "":
        return "Pending"
    
    if ("(" in endstate):
        eslist = endstate.split('(')
        return eslist[0].strip()
    else:
        return endstate

def clean_date_field(date):
    if not isinstance(date, str):
        return None
    
    if date == '':
        return None
    
    if (("/" not in date) or len(date) < 8):
        return None

    datelist = date.split('/')
    datelist[2] = "20" + datelist[2]
    dateobj = datetime.date(int(datelist[2]), int(datelist[0]), int(datelist[1])) 

    return dateobj

def days_between_dates(date1, date2):
    if (date1 == None or date2 == None):
        return None
    
    return (date2 - date1).days

def classify_job_level(title):
    if not isinstance(title, str):
        return 99
    
    if (("VP" in title) or ("Vice" in title) or ("Head" in title)):
        return 5
    elif ("Director" in title):
        if ("Senior" in title):
            return 4
        else:
            return 3
    elif ("Manager" in title):
        if ("Senior" in title):
            return 2
        else:
            return 1
    else:
        return 99 #something has broken my classification logic
    
def classify_job_type(title):
    if not isinstance(title, str):
        return 99

    if (("Engineering" in title) or ("Technology" in title) or ("Development" in title) or ("Platforms" in title)):
        return 1
    elif ("Product" in title):
        return 2
    elif ("Program" in title):
        return 3
    elif ("Business" in title):
        return 4
    else:
        return 99 #something has broken my classification logic