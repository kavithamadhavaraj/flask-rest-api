
class DataStore(object):

    def __init__(self): # this method creates the class object.
        self.__employee_data = [
        {'date': '2017-03-01', 'dept': 'Sales', 'employee': 3, 'salary': 70000},
        {'date': '2015-03-01', 'dept': 'Engineering', 'employee': 4, 'salary': 45000},
        {'date': '2017-09-01', 'dept': 'Sales', 'employee': 4, 'salary': 60000},
        {'date': '2016-03-01', 'dept': 'Sales', 'employee': 5, 'salary': 40000},
        {'date': '2017-12-01', 'dept': 'Support', 'employee': 5, 'salary': 65000},
        {'date': '2016-02-01', 'dept': 'Support', 'employee': 5, 'salary': 40000},
        {'date': '2016-03-01', 'dept': 'Support', 'employee': 6, 'salary': 70000},
        {'date': '2016-11-01', 'dept': 'Engineering', 'employee': 6, 'salary': 45000},
        {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 7, 'salary': 70000},
        {'date': '2015-09-01', 'dept': 'Sales', 'employee': 7, 'salary': 55000},
        {'date': '2017-11-01', 'dept': 'Support', 'employee': 7, 'salary': 50000},
        {'date': '2015-08-01', 'dept': 'Engineering', 'employee': 7, 'salary': 65000},
        {'date': '2015-08-01', 'dept': 'Engineering', 'employee': 8, 'salary': 60000},
        {'date': '2017-11-01', 'dept': 'Sales', 'employee': 9, 'salary': 55000},
        {'date': '2015-01-01', 'dept': 'Support', 'employee': 9, 'salary': 55000},
        {'date': '2017-12-01', 'dept': 'Engineering', 'employee': 10, 'salary': 55000},
        {'date': '2016-12-01', 'dept': 'Sales', 'employee': 10, 'salary': 50000},
        {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 10, 'salary': 70000},
        {'date': '2016-11-01', 'dept': 'Support', 'employee': 11, 'salary': 75000},
        {'date': '2016-08-01', 'dept': 'Sales', 'employee': 12, 'salary': 40000},
        {'date': '2016-06-01', 'dept': 'Engineering', 'employee': 12, 'salary': 40000},
        {'date': '2015-01-01', 'dept': 'Sales', 'employee': 12, 'salary': 40000},
        {'date': '2015-11-01', 'dept': 'Support', 'employee': 12, 'salary': 45000},
        {'date': '2016-03-01', 'dept': 'Sales', 'employee': 13, 'salary': 60000},
        {'date': '2015-01-01', 'dept': 'Engineering', 'employee': 13, 'salary': 70000},
        {'date': '2017-08-01', 'dept': 'Engineering', 'employee': 13, 'salary': 75000},
        {'date': '2015-12-01', 'dept': 'Sales', 'employee': 14, 'salary': 60000},
        {'date': '2017-07-01', 'dept': 'Support', 'employee': 16, 'salary': 60000},
        {'date': '2016-12-01', 'dept': 'Engineering', 'employee': 17, 'salary': 45000},
        {'date': '2017-11-01', 'dept': 'Engineering', 'employee': 18, 'salary': 45000},
        {'date': '2015-03-01', 'dept': 'Engineering', 'employee': 20, 'salary': 45000},
        {'date': '2016-06-01', 'dept': 'Sales', 'employee': 21, 'salary': 40000},
        {'date': '2016-09-01', 'dept': 'Engineering', 'employee': 21, 'salary': 70000},
        {'date': '2016-01-01', 'dept': 'Engineering', 'employee': 23, 'salary': 50000},
        {'date': '2016-02-01', 'dept': 'Engineering', 'employee': 23, 'salary': 75000},
        {'date': '2017-04-01', 'dept': 'Engineering', 'employee': 24, 'salary': 55000},
        {'date': '2016-09-01', 'dept': 'Engineering', 'employee': 25, 'salary': 50000},
        {'date': '2017-05-01', 'dept': 'Sales', 'employee': 28, 'salary': 60000},
        {'date': '2017-10-01', 'dept': 'Support', 'employee': 29, 'salary': 40000},
        {'date': '2017-06-01', 'dept': 'Engineering', 'employee': 30, 'salary': 70000}]

    def run_query(self):
        return self.__employee_data

