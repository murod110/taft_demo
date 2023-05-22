import requests
import json


BASE_URL = 'https://fd63-213-230-72-238.ngrok-free.app/api/v1'

def create_user(username,name,user_id):
    url = f"{BASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    list = []
    for i in data:
        list.append(i["user_id"])
    if user_id not in list:
        requests.post(url=url, data={"username":username,"name":name,"user_id":user_id})

  
def create_feedback(user_id, body):
    url = f"{BASE_URL}/bot-feedback"
    if body and user_id:
        requests.post(url=url, data = {"user_id":user_id,"body":body})
        return "Adminga jo'natildi. Fikringiz uchun tashakkur. "
    else:
        return "Amal oxiriga yetmadi. "

def get_product(type):
    url = f"{BASE_URL}/product-api"
    response = requests.get(url=url).text
    data = json.loads(response)
    datas = {}
    for d in data:
        if type == "🪡🧶 Tufting" and d["quality"]["cat"]["id"]==1:
            datas[d["design"]["palet"]["name"]]=d["design"]["palet"]["id"]
        elif type == "🖨 Printed" and d["quality"]["cat"]["id"]==2:
            datas[d["design"]["palet"]["name"]]=d["design"]["palet"]["id"]
        elif type == "🏟 Grass" and d["quality"]["cat"]["id"]==3:
            datas[d["design"]["palet"]["name"]]=d["design"]["palet"]["id"] 
        elif type == "🛁 Bath Mats" and d["quality"]["cat"]["id"]==4:
            datas[d["design"]["palet"]["name"]]=d["design"]["palet"]["id"] 
    return datas

def get_palet(id):
    url = f"{BASE_URL}/palet"
    response = requests.get(url=url).text
    data = json.loads(response)
    for p in data:
        if p["pk"]==id:
            return p["name"]


def get_carpet_id(id):
    url = f"{BASE_URL}/product-api"
    response = requests.get(url=url).text
    data = json.loads(response)
    date = []
    for p in data:
        if p["design"]["palet"]["id"]==id:
            date.append(p)
    return date


def get_prod_id(id):
    url = f"{BASE_URL}/product-api"
    response = requests.get(url=url).text
    data = json.loads(response)
    date = []
    for p in data:
        if p["design"]["name"]==id:
            date.append(p)
    return date