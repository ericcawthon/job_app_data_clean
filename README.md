## About the Code
Python script for cleaning up formatting of job application data sheet and calculating duration between events.  The script takes a raw .csv file as an input and outputs a cleaned up .csv file that can be used to import and analyze with the user's tool of choice.

## Python libraries needed
pandas

## Usage
1. Put job search data .csv file in the /input folder (a template is included here)
2. Execute the script by providing the .csv filename as an argument (ex. `python3 job_search_summarize.py --inputfilename job_search_data.csv`)
3. The script outputs a new .csv file in the /output folder with "clean_" appended to the input file name as the output filename (ex. "job_search_data.csv" > "clean_job_search_data.csv")
