from fastapi import FastAPI
import db
import modals

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello Uddesh"}


@app.get("/all")
def get_all():
    data = db.all()
    return {"data":data}

@app.post("/create")
def create(data:modals.Todo):
    id = db.create(data)
    return {"inserted":True,"inserted_id":id }

@app.get("/get/{}")
def get_one(name:str):
    data = db.get_one(name)
    return {"data":data}

@app.delete("/delete")

def delete(name:str):           
    data = db.delete(name)
    return {"deleted":True,"deleted_count":data}

@app.put("/update")

def update(name:str,data:modals.Todo):  
    data = modals.Todo(name = data.name,description=data.description)
    data = db.update(data)
    return {"updated":True,"updated_count":data}