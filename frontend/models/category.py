import json
import requests
from .constants import SERVER_URL

class category:
    ENDPOINT = "/category/"

    def __init__( self , id_category=None, category_name=None):
        self.id_category =id_category
        self.category_name =category_name

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {
        'category_name':self.category_name,
        'id_category':self.id_category,
        }
    
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)

        data = json.loads(response.text)
        self.id = data['id']

    def read(id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += id if id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if id:
            category = __class__(**response)
            return category
        else:
            category = []

            for result in response:
                category = __class__(**result)
                categories.append(category)
            
            return categories
            
    def delete(self ,id):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.id = None
        except Exception:
            raise Exception