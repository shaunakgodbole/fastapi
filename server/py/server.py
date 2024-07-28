import os

import fastapi
import uvicorn

app = fastapi.FastAPI()

count = 1
@app.get("/hello")
async def counter():
    global count
    count = count + 1
    print("The count is: ", count)
    return "hello world {}".format(count)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
