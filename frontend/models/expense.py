import json
import requests
from .constants import SERVER_URL

class Expense:
    ENDPOINT = "/expense/"

    def __init__(self, item=None, amount=None, date=None, reason=None ):
        self.item =item
        self.amount =amount
        self.date =date
        self.reason =reason

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {
        'item' :self.item,
        'amount' :self.amount,
        'date' :self.date,
        'reason' :self.reason
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
            expense = __class__(**response)
            return expense
        else:
            expenses = []

            for result in response:
                expense = __class__(**result)
                expenses.append(expense)
            
            return expenses

    def delete(self ,id=None):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.id = None
        except Exception:
            raise Exception