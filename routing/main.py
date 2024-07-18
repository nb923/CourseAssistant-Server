import pandas as pd
from fastapi import FastAPI

print(pd.__version__)

Data_Dictionary = pd.read_excel('/Users/josesantiago/Downloads/Data Values/DataDictionary.xlsx')
print(Data_Dictionary.head())

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}