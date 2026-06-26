from fastapi import FastAPI

from routers import company,job
app = FastAPI()

app.include_router(company.router)
app.include_router(job.router)

@app.get("/about")
def read_about():
    return {"About": "This is about page"}

@app.get("/contacts")
def read_contacts():
    return {"Contacts": "This is contacts page"}

@app.get("/info")
def read_info():
    return {"Info": "This is info page"}

@app.get("/admin")
def read_admin():
    return {"Admin": "This is admin page"}