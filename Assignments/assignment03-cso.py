import pandas as pd
import json

# Took a bit of finding to locate the necessary url
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
df = pd.read_json(url)
data = df.to_json()
with open("cso.json", "w") as f:
    f.write(data)