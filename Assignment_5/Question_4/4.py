dict = {
    "Noida": 300000,
    "Delhi": 500000,
    "Mumbai": 700000
};

import io
import json
with io.open("cities.json", "w") as f:
    json.dump(dict, f);

with io.open("cities.json", "r") as f:
    obj = json.load(f);
    print(obj);
