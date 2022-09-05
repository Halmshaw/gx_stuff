import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    player= req.params.get('player')

    if not name or player:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            player= req.params.get('player')

    if name and player:
        return func.HttpResponse(f"Hello, {name} {player}. This HTTP triggered function executed successfully.")
    
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name and a player in the query string or in the request body for a personalized response.",
             status_code=200
        )