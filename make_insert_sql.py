import pandas
import numpy as np
import argparse

def handle_null(value):
    if value == "null":
        return value + ", "
    else:
        return  "'" + value + "', "

parser = argparse.ArgumentParser()
parser.add_argument('--inputfiledate', dest='inputfiledate', type=str, help='provide input filename date')
args = parser.parse_args()

create_sql = """CREATE TABLE `applications_{file_date}` (
  `id` int(10) NOT NULL,
  `company` varchar(255) NOT NULL,
  `job_title` varchar(255) NOT NULL,
  `listed_top_pay` int(7) DEFAULT NULL,
  `discovered` date DEFAULT NULL,
  `posted` date DEFAULT NULL,
  `applied` date DEFAULT NULL,
  `response` date DEFAULT NULL,
  `closed` date DEFAULT NULL,
  `end_state` varchar(255) NOT NULL,
  `interviewers` int(3) DEFAULT NULL,
  `job_level_id` int(3) NOT NULL,
  `job_type_id` int(3) NOT NULL,
  `days_posted_to_applied` int(3) DEFAULT NULL,
  `days_applied_to_response` int(3) DEFAULT NULL,
  `days_response_to_closed` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8; \n
ALTER TABLE `applications_{file_date}`
  ADD PRIMARY KEY (`id`); \n
ALTER TABLE `applications_{file_date}` CHANGE `id` `id` INT(10) NOT NULL AUTO_INCREMENT; \n""".format(file_date=args.inputfiledate)

insert_sql = "INSERT INTO `applications_{file_date}` (company, job_title, listed_top_pay, discovered, posted, applied, response, closed, end_state, interviewers, job_level_id, job_type_id, days_posted_to_applied, days_applied_to_response, days_response_to_closed) VALUES \n".format(file_date=args.inputfiledate)

df_raw = pandas.read_csv('output/clean_job_search_data_' + args.inputfiledate + '.csv')
df = df_raw.replace(np.nan, 'null', regex=True)

for index, row in df.iterrows():
    if row['Company'] == "null":
        break
    insert_sql = insert_sql + "("
    insert_sql = insert_sql + "'" + str(row['Company']) + "', "
    insert_sql = insert_sql + "'" + str(row['Job Title']) + "', " 
    insert_sql = insert_sql + str(row['Listed Top Pay']) + ", "
    insert_sql = insert_sql + handle_null(str(row['Discovered']))
    insert_sql = insert_sql + handle_null(str(row['Posted']))
    insert_sql = insert_sql + handle_null(str(row['Applied']))
    insert_sql = insert_sql + handle_null(str(row['Response']))
    insert_sql = insert_sql + handle_null(str(row['Closed']))
    insert_sql = insert_sql + "'" + str(row['End State']) + "', "
    insert_sql = insert_sql + str(row['Interviewers']) + ", "
    insert_sql = insert_sql + str(row['Job Level']) + ", "
    insert_sql = insert_sql + str(row['Job Type']) + ", "
    insert_sql = insert_sql + str(row['Days Posted to Applied'])
    insert_sql = insert_sql + ", " + str(row['Days Applied to Response']) + ", "
    insert_sql = insert_sql + str(row['Days Response to Closed']) 
    insert_sql = insert_sql + "), \n"

insert_sql = insert_sql[:-3] + ";"

outfilename = "output/" + args.inputfiledate + ".txt"
outfile = open(outfilename, 'w')
outfile.write(create_sql)
outfile.write(insert_sql)
outfile.close()