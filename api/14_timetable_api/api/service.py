from fastapi import FastAPI
from .models import GetTimetableApiRequest, SetTimetableApiRequest, ResetTimetableApiRequest
from database import Database
from config import Config
from database import DatabaseException
from fastapi.responses import JSONResponse
from http import HTTPStatus

app = FastAPI()
config: Config
database: Database


@app.on_event('startup')
def on_startup():
    global database, config
    config = Config()
    database = Database()


@app.post("/get_timetable")
def get_timetable(api_request: GetTimetableApiRequest):
    try:
        lessons = database.get_timetable(request=api_request)
        result = JSONResponse(status_code=HTTPStatus.OK, content=lessons)
    except DatabaseException as err:
        result = JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=err.message)
    return result


@app.post("/set_timetable")
def set_timetable(api_request: SetTimetableApiRequest):
    try:
        database.set_timetable(request=api_request)
        result = JSONResponse(status_code=HTTPStatus.OK, content="successfully created")
    except DatabaseException as err:
        result = JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=err.message)
    return result


@app.post("/reset_timetable")
def reset_timetable(api_request: ResetTimetableApiRequest):
    try:
        database.reset_timetable()
        result = JSONResponse(status_code=HTTPStatus.OK, content="successfully cleared")
    except DatabaseException as err:
        result = JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=err.message)
    return result