from enum import Enum
from typing import Optional
from fastapi import FastAPI

class QueryModel(str, Enum):
    country_code = "SVN"

app = FastAPI()

fake_db = {
    "countries": [
        { 
            "name": "Slovenia", 
            "country_iso_code": "SVN", 
            "key": "new_deaths",
            "chat_data": [
                19,
                46,
                65,
                88,
                108,
                130,
                143,
                162,
                181,
                204,
                220,
                235,
                252,
                263,
                275,
                294,
                307,
                317
            ]
        },
        { 
            "name": "Croatia", 
            "country_iso_code": "HRV", 
            "key": "new_deaths",
            "chat_data": [
                32,
                55,
                86,
                116,
                145,
                171,
                200,
                227,
                244,
                261,
                279,
                295,
                317,
                342,
                371,
                397,
                411,
                436
            ]
        },
        { 
            "name": "United Kingdom", 
            "country_iso_code": "GBR", 
            "key": "new_deaths",
            "chat_data": [
                594,
                2230,
                3956,
                5195,
                6443,
                7648,
                8238,
                8645,
                10096,
                11418,
                12333,
                13348,
                14176,
                14552,
                14885,
                15937,
                16939,
                17619
            ]
        },
    ],
    "total_death": [
        [
            1611532800,
            1611619200,
            1611705600,
            1611792000,
            1611878400,
            1611964800,
            1612051200,
            1612137600,
            1612224000,
            1612310400,
            1612396800,
            1612483200,
            1612569600,
            1612656000,
            1612742400,
            1612828800,
            1612915200,
            1613001600
        ]        
    ]
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/query/country_code={country_code}&total_death={total_death}")
async def get_query(country_code: str, total_death: bool):
    item = {
        "country": { "name": "", "country_code": "", "key": "", "chat_data": [] },
        "total_death": []
    }
    for x in fake_db["countries"]:
        if x["country_iso_code"] == country_code:
            item["country"]["name"] = x["name"]
            item["country"]["country_code"] = x["country_iso_code"]
            item["country"]["key"] = x["key"]
            item["country"]["chat_data"] = x["chat_data"]
            if total_death:
                item["total_death"] = fake_db["total_death"]
            break
    return item