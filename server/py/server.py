import os

import fastapi
from fastapi import Request
import uvicorn


app = fastapi.FastAPI()
@app.middleware("http")
async def add_custom_logic_middlewear(request: Request, call_next):
    if request.url.path == "/hello":
        print("Executing function before")
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            raise e
        finally:
            print("Executing function after")

count = 1
@app.get("/hello")
async def counter():
    global count
    count = count + 1
    print("The count is: ", count)
    if count % 5 == 0:
        raise Exception("This is exceptional!")
    return "hello world {}".format(count)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
