# def calc_interviewers_met(endstate):
#     if not isinstance(endstate, str):
#         return None

#     if endstate == "":
#         return None
    
#     if ("(" in endstate):
#         eslist = endstate.split('(')
#         return int(eslist[1][:len(eslist)-1])
#     else:
#         return 0

# def clean_end_state(endstate):
#     if not isinstance(endstate, str):
#         return "Pending"

#     if endstate == "":
#         return "Pending"
    
#     if ("(" in endstate):
#         eslist = endstate.split('(')
#         return eslist[0].strip()
#     else:
#         return endstate

# def clean_date_field(date):
#     if not isinstance(date, str):
#         return None
    
#     if date == '':
#         return None
    
#     if (("/" not in date) or len(date) < 8):
#         return None

#     datelist = date.split('/')
#     datelist[2] = "20" + datelist[2]
#     dateobj = datetime.date(int(datelist[2]), int(datelist[0]), int(datelist[1])) 

#     return dateobj

# def days_between_dates(date1, date2):
#     if (date1 == None or date2 == None):
#         return None
    
#     return (date2 - date1).days

# def classify_job_level(title):
#     if not isinstance(title, str):
#         return 99
    
#     if (("VP" in title) or ("Vice" in title) or ("Head" in title)):
#         return 5
#     elif ("Director" in title):
#         if ("Senior" in title):
#             return 4
#         else:
#             return 3
#     elif ("Manager" in title):
#         if ("Senior" in title):
#             return 2
#         else:
#             return 1
#     else:
#         return 99 #something has broken my classification logic
    
# def classify_job_type(title):
#     if not isinstance(title, str):
#         return 99

#     if (("Engineering" in title) or ("Technology" in title) or ("Development" in title) or ("Platforms" in title)):
#         return 1
#     elif ("Product" in title):
#         return 2
#     elif ("Program" in title):
#         return 3
#     elif ("Business" in title):
#         return 4
#     else:
#         return 99 #something has broken my classification logic

import pandas
# import datetime
import functions
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inputfilename', dest='inputfilename', type=str, help='provide input filename')
args = parser.parse_args()
df = pandas.read_csv('input/' + args.inputfilename)

# break out new field for number of interviewers met and cleanup End State field
df['Interviewers'] = df.apply(lambda row : functions.calc_interviewers_met(row['End State']), axis=1)
df['End State'] = df.apply(lambda row : functions.clean_end_state(row['End State']), axis=1)

# set Job Level and Job Type baesd on the Job Title
df['Job Level'] = df.apply(lambda row : functions.classify_job_level(row['Job Title']), axis=1)
df['Job Type'] = df.apply(lambda row : functions.classify_job_type(row['Job Title']), axis=1)

# cleanup all the date fields
df['Discovered'] = df.apply(lambda row : functions.clean_date_field(row['Discovered']), axis=1)
df['Posted'] = df.apply(lambda row : functions.clean_date_field(row['Posted']), axis=1)
df['Applied'] = df.apply(lambda row : functions.clean_date_field(row['Applied']), axis=1)
df['Response'] = df.apply(lambda row : functions.clean_date_field(row['Response']), axis=1)
df['Closed'] = df.apply(lambda row : functions.clean_date_field(row['Closed']), axis=1)

# calculate days elapsed between key dates
df['Days Posted to Applied'] = df.apply(lambda row : functions.days_between_dates(row['Discovered'], row['Applied']), axis=1)
df['Days Applied to Response'] = df.apply(lambda row : functions.days_between_dates(row['Applied'], row['Response']), axis=1)
df['Days Response to Closed'] = df.apply(lambda row : functions.days_between_dates(row['Response'], row['Closed']), axis=1)


#i = 100
#print(days_between_dates(df.iloc[i]['Discovered'], df.iloc[i]['Applied']))

#print(type(df.iloc[i]['Discovered']))
#print(type(df.iloc[i]['Days Posted to Applied']))
# print(df.loc[df['Job Type'] == 99])

# print(df.groupby(by='Job Type', dropna=False)['Job Type'].count())

# by_end = df.groupby(by='End State', dropna=False)['End State'].count()
# print(by_end)

df.to_csv('output/clean_' + args.inputfilename, index=False)