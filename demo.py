from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

print(os.listdir("slides"))

html = f"""
<!DOCTYPE html>
<html>
    <body>
    {
        "".join([f"<a href='/slides/{s}'>{s}</a>" for s in os.listdir("slides")])
    }
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

for s in os.listdir("slides"):
    app.mount(f"/slides/{s}", StaticFiles(directory=f"slides/{s}", html=True), name="demo")


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
