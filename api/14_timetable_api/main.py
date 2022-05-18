from api.service import app
import uvicorn
from config import Config
from database.database import Database
from api.models import GetTimetableApiRequest, SetTimetableApiRequest


if __name__ == '__main__':
    config = Config(filename='config.yaml')

    uvicorn.run(
        app=app,
        host=config.ENDPOINT_HOST,
        port=config.ENDPOINT_PORT,
        log_level=config.LOG_LEVEL
    )


    # db = Database()
    # get_request = GetTimetableApiRequest(faculty='test_faculty',
    #                                      group='test_group',
    #                                      week_num=1,
    #                                      day_num=1)
    # set_request = SetTimetableApiRequest(faculty_tag='fet',
    #                                      group_name='v-51p',
    #                                      week_num=32,
    #                                      day_num=3,
    #                                      time_cell_num=4,
    #                                      discipline_type='examine',
    #                                      discipline_name='informatics',
    #                                      teacher_full_name='Ivanov A.A.',
    #                                      room_name='1-623')
    # timetable = db.set_timetable(params=set_request)
