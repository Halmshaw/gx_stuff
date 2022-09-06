import datetime 
import calendar
import logging
import json
import azure.functions as func



def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> str:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    
    # todayDate = datetime.date.today()
    # if todayDate.day > 25:
    #     todayDate += datetime.timedelta(7)

    # def last_day_of_month(d: datetime.date) -> datetime.date:
    #     return (
    #         datetime.date(d.year + d.month//12, d.month % 12 + 1, 1) -
    #         datetime.timedelta(days=1)
    #     )
           
    current_date = datetime.date.today()
    first_day_of_month = datetime.date(current_date.year, current_date.month, 1)
    last_day_of_month = datetime.date(current_date.year, current_date.month, calendar.monthrange(current_date.year, current_date.month)[1])
 
    strFirst = first_day_of_month.strftime("%d/%m/%Y")
    strLast = last_day_of_month.strftime("%d/%m/%Y")
    value =  {
        "firstDateOfMonth": strFirst,
        "lastDateOfMonth": strLast
    }




    print(json.dumps(value)) 

    # print(first_day_of_month)
    # print(last_day_of_month)
    
    return func.HttpResponse( json.dumps(value))
        #msg.set(name)
    

