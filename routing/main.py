import pandas as pd
from fastapi import FastAPI
import os
from dovenv import load_dotenv

load_dotenv()

print(pd.__version__)



Data_Dictionary = pd.read_excel(os.getenv('DATA_DICT_PATH'))

SASCourseNotes_SubjectNotes = pd.read_excel(os.getenv('COURSE_NOTES_PATH'))

SASCourseCodes = pd.read_excel(os.getenv('COURSE_CODES_PATH'))

SASCoursesCoreCodes_PreReq = pd.read_excel(os.getenv('COURSE_PREREQS_PATH'))

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}