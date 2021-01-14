import os
from typing import Optional
from requests import post
from fastapi import FastAPI

app = FastAPI()

ha_ip = os.environ['HA_IP']
ha_port = os.environ['HA_PORT']
ha_entity = os.environ['HA_ENTITY']
ha_token = os.environ['HA_TOKEN']
ha_brightness = os.environ['HA_BRIGHTNESS']
ha_domain = ha_entity.split('.')[0]


base_url = str("http://" + ha_ip + ":" + ha_port + "/api/services/" + ha_domain + "/")
headers = {
    "Authorization": str("Bearer " + ha_token),
    "Content-Type": "application/json"
}

def payload_color(color_name):
    payload = {
        "entity_id": ha_entity,
        "color_name": color_name,
        "brightness": ha_brightness
    }
    return payload

@app.post("/available")
def available():
    url = base_url + "turn_on"
    post(url, headers=headers, json=payload_color("green"))
    
@app.post("/busy")
def busy():
    url = base_url + "turn_on"
    post(url, headers=headers, json=payload_color("red"))

@app.post("/away")
def away():
    url = base_url + "turn_on"
    post(url, headers=headers, json=payload_color("yellow"))

@app.post("/offline")
def offline():
    url = base_url + "turn_off"
    payload = {
        "entity_id": ha_entity
    }
    post(url, headers=headers, json=payload)