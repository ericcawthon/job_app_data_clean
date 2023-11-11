import pandas
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


df.to_csv('output/clean_' + args.inputfilename, index=False)