from fastapi import FastAPI, Request
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE = os.path.join(os.path.dirname(__file__), "people.db")
db = create_engine("sqlite:///" + DATABASE)

def get_age(name:str):
    with db.connect() as conn:
        res = conn.execute(text("select age from people where name = :name"),
              {"name":name}).fetchone()
        if res:
             return res[0]
        else:
            raise NotFound("NotFound")
            
            
class person(BaseModel):
    name:str = "abc"
    format:str ="json"
    
class NotFound(Exception):
    pass
    
@app.get("/helloj") 
@app.get("/helloj/{name}/{format}")
def helloj_get(name:str="abc", format:str="json"):  
    fformat = format
    fname = name
    try:
        age = get_age(fname)
        return {"name":fname, "age":age}
    except NotFound:
        return {"name":fname, "details":"Not found"}
 
@app.post("/helloj") 
def helloj_post(data: person):
    fname = data.name
    fformat = data.format
    try:
        age = get_age(data.name)
        return {"name":fname, "age":age}
    except NotFound:
        return {"name":fname, "details":"Not found"}
        
if __name__ == '__main__':
    #http://localhost:5000
    app.run()
    