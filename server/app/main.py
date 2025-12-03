# ltb-parametric-guitar - Server Entry Point
# Extract features from golden master as needed
# Golden Master: https://github.com/HanzoRazer/luthiers-toolbox

from fastapi import FastAPI

app = FastAPI(
    title=""LTB Parametric Guitar Designer - Body shape generator and template exporter"",
    version=""0.1.0""
)

@app.get("/")
def read_root():
    return {"status": "ready", "edition": "PARAMETRIC"}
