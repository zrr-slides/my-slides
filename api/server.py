from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

slides_path = "./slides"
slides = os.listdir(slides_path)
html = f"""
<!DOCTYPE html>
<html>
    <body>
    {
        "".join([f"<a href='/slides__{s}'>{s}</a>" for s in slides])
    }
    </body>
</html>
"""

for s in slides:
    app.mount(
        f"/slides__{s}",
        StaticFiles(directory=f"{slides_path}/{s}", html=True),
        name=s,
    )


@app.get("/")
async def root():
    return HTMLResponse(html)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
