import datetime #imports the module of date and time into python 
import calendar #Imports the calendar data into python 
import logging #is used to log messages you want to be able to see
import json #converts python dictionary into a Json string
import azure.functions as func # Allows the code to connect to the Azure cloud



def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> str: #def is used to define the main function, 
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name') #turns req.params.get into a variable 
    if not name: #it checks if the statement is true or not 
        try: 
            req_body = req.get_json()
        except ValueError:
            pass
        else:  
            name = req_body.get('name') #if the statement is correct the name will be displayed 
    
    # todayDate = datetime.date.today()
    # if todayDate.day > 25:
    #     todayDate += datetime.timedelta(7)

    # def last_day_of_month(d: datetime.date) -> datetime.date:
    #     return (
    #         datetime.date(d.year + d.month//12, d.month % 12 + 1, 1) -
    #         datetime.timedelta(days=1)
    #     )
           
    current_date = datetime.date.today() #turned the value into an variable 
    first_day_of_month = datetime.date(current_date.year, current_date.month, 1) #
    last_day_of_month = datetime.date(current_date.year, current_date.month, calendar.monthrange(current_date.year, current_date.month)[1])
 
    strFirst = first_day_of_month.strftime("%d/%m/%Y") # turns the data into a variable
    strLast = last_day_of_month.strftime("%d/%m/%Y")   # turns the data into a variable
    value =  {
        "firstDateOfMonth": strFirst,
        "lastDateOfMonth": strLast
    }




    print(json.dumps(value)) #prints the first and last day of the month 

    # print(first_day_of_month)
    # print(last_day_of_month)
    
    return func.HttpResponse( json.dumps(value)) #this sends the functions results back to the programmer 
        #msg.set(name)
    

