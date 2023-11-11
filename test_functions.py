import functions
import pytest
import datetime

@pytest.mark.interviewers_met
def test_calc_interviewers_met():
    assert functions.calc_interviewers_met(7) == None
    assert functions.calc_interviewers_met("") == None
    assert functions.calc_interviewers_met("No offer (4)") == 4
    assert functions.calc_interviewers_met("No offer ") == 0

@pytest.mark.clean_end_state
def test_clean_end_state():
    assert functions.clean_end_state(True) == "Pending"
    assert functions.clean_end_state("") == "Pending"
    assert functions.clean_end_state("Recruiter Screen") == "Recruiter Screen"
    assert functions.clean_end_state("Recruiter Screen (1)") == "Recruiter Screen"

@pytest.mark.clean_date_field
def test_clean_date_field():
    assert functions.clean_date_field("10/07/23") == datetime.date(2023, 10, 7)
    assert functions.clean_date_field("11/23/23") == datetime.date(2023, 11, 23) 
    assert functions.clean_date_field(2023) == None
    assert functions.clean_date_field("") == None

@pytest.mark.days_between_dates
def test_days_between_dates():
    assert functions.days_between_dates(datetime.date(2023, 10, 7), datetime.date(2023, 11, 23)) == 47
    assert functions.days_between_dates(datetime.date(2023, 11, 7), datetime.date(2023, 11, 14)) == 7
    assert functions.days_between_dates(datetime.date(2023, 11, 7), None) == None
    assert functions.days_between_dates(None, datetime.date(2023, 4, 7)) == None

@pytest.mark.classify_job_level
def test_classify_job_level():
    assert functions.classify_job_level("") == 99
    assert functions.classify_job_level(14) == 99
    assert functions.classify_job_level("Vice President of Technology") == 5
    assert functions.classify_job_level("VP of Engineering") == 5
    assert functions.classify_job_level("Head of Product") == 5
    assert functions.classify_job_level("President of Technology") == 99
    assert functions.classify_job_level("Senior Director of Engineering") == 4
    assert functions.classify_job_level("Director of Technology") == 3
    assert functions.classify_job_level("Senior Manager, Software Engineering") == 2
    assert functions.classify_job_level("Product Manager") == 1
    assert functions.classify_job_level("Software Engineer") == 99

@pytest.mark.classify_job_type
def test_classify_job_type():
    assert functions.classify_job_type("") == 99
    assert functions.classify_job_type(14) == 99
    assert functions.classify_job_type("Engineering") == 1
    assert functions.classify_job_type("Technology") == 1
    assert functions.classify_job_type("Product") == 2
    assert functions.classify_job_type("Program") == 3
    assert functions.classify_job_type("Tech") == 99