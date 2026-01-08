from fastapi import FastAPI

app=FastAPI()

## decoretor to make the function run when calling the api
@app.get("/")
## async means that the function can run more-less then the times that the functions do
async def root():
    return {"message": "Welecome to your First API in FastAPI"}
