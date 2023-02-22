from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.exception_handler(HTTPException)
def http_exception_handler(request, exc):
    if 500 <= exc.status_code < 600:
        response = requests.post('https://external-service.com/notification', json={'message': f'Internal server error: {exc.detail}'})
        return JSONResponse(status_code=exc.status_code, content={'error': 'Internal server error'})
    return exc

app.get('/cause-error')
def cause_error():
    raise HTTPException(status_code=500, detail='sth went wrong!!!')