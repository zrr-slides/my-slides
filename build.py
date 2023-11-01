import os
import shutil


slides = os.listdir("./slides")


os.makedirs("./build", exist_ok=True)
shutil.copy("./slides", "./build/slides")
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
with open("./build/index.html", "w") as f:
    f.write(html)
