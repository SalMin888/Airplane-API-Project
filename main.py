import requests
from fastapi import FastAPI


app = FastAPI()

API_KEY = "9359e7f4b92aacc1aaf4914925a53a46"

@app.get("/airplanemodel")
def get_model(model_code: str):
    url = f"https://api.aviationstack.com/v1/airplanes?access_key={API_KEY}"
    response = requests.get(url, timeout=5)
    data_1 = response.json()
    history = data_1.get("data")[0]
    return {"model_code": model_code, 'id': history.get("id"), 
                'construction_number': history.get('construction_number'), 
                'engines_type': history.get('engines_type'),
                'plane_age': history.get('plane_age'),
                'plane_owner': history.get('plane_owner'),
                'plane_status': history.get('plane_status'), 
                'production_line': history.get('production_line')}

            
# use uvicron
# https://aviationstack.com/quickstart
    
