import datetime 
import logging
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

    todayDate = datetime.date.today()
    if todayDate.day > 25:
        todayDate += datetime.timedelta(7)
    lastDayOfMonth = datetime.date(currentDate.year, currentDate.month, 1)
    
    print(todayDate.replace(day=1))
    print(lastDayOfMonth)
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        #msg.set(name)

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )