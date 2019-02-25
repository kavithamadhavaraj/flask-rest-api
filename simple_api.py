import pandas as pd
from flask import Flask, request, Response, jsonify
from datastore import DataStore

app = Flask(__name__)
#Intialisation of the DataStore object
data_store_obj = DataStore()

#Route that lists all the available endpoints
@app.route('/', methods = ['GET'])
def welcome():
    routes = {}
    for r in app.url_map._rules:
        routes[r.rule] = {}
        routes[r.rule]["methods"] = list(r.methods)
    routes.pop("/static/<path:filename>")
    return jsonify(routes)

@app.route('/averages', methods = ['GET'])
def get_average_current_salary_by_department():
    query_result = pd.DataFrame(data_store_obj.run_query())
    #Sort the dataframe by date to get the recent salaries of the employees
    query_result.sort_values(['date'],ascending=False, inplace=True)
    #Keep only the recent salaries
    query_result.drop_duplicates(["employee"], keep='first', inplace=True)
    #Groupby department and find the average
    response_obj = query_result.groupby(['dept'])['salary'].mean()
    return Response(response_obj.to_json(), mimetype='application/json')


def monthly_count(row, query_result):
    #Count the employees who start date and end date within "this" month 
    count = query_result[(query_result["date"]<=row.month) & ((query_result["end_date"].isnull()) | (row.month < query_result["end_date"]))]
    return len(count)

@app.route('/headcount_over_time', methods = ['GET'])
def get_monthly_headcount():
    #Extract the department URL parameter, if present. Otherwise defaults to None
    department = request.args.get('department', default = None, type = str)
    query_result = pd.DataFrame(data_store_obj.run_query())
    if len(query_result) == 0:
        #If no records for the provided department is found, display the information to user along with 404
        return Response("No data found for the department ["+department+"]. Try again with the valid one.", status=404)
    query_result["date"] = pd.to_datetime(query_result["date"], format="%Y-%m-%d")
    #Find the start date and end date from the dataset, for report generation
    min_date, max_date = query_result["date"].min(), query_result["date"].max()
    #Generate all the months within the start date and end date
    datelist = pd.DataFrame({"month":(pd.date_range(start=min_date, end=max_date, freq="MS"))})
    #Sort the query result based on employee id and date
    query_result.sort_values(["employee","date"],inplace=True)
    #Find the end date of each of the employee's current status
    #If an employee didn't switch without payrise, end_date will be NaT
    #If an employee switched, end_date will be the switched date
    #If an employee got payrise, end_date will be the date in which he got payrise    
    query_result["end_date"] = query_result.groupby(["employee"])["date"].transform(lambda x:x.shift(-1))
    if department != None:
        #Remove the other department records
        query_result = query_result[query_result["dept"]==department]
    #For each month in the reporting list, get the headcount
    datelist["headcount"] = datelist.apply(lambda x: monthly_count(x, query_result), axis=1)
    #Some formatting changes 
    datelist["month"] = datelist["month"].astype(str)
    response_obj = {"data" : datelist.to_dict(orient='records')}
    #Jsonify set the content-type as 'application/json automatically'
    return jsonify(response_obj)
    
if __name__ == '__main__':
    app.run(debug=True, port=9999)
