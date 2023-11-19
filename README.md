# CS361MicroServiceProject
Exampl UML Diagram: 

<img width="479" alt="image" src="https://github.com/RubenBravoLugo/CS361MicroServiceProject/assets/71678992/8325c7c9-b624-41fe-949b-aeb299c849cb">


# Request Data
Requesting involves:  
- calling post by: response = requests.post(url, json=data), with the prvided webhook link.
- https://graciousjadedobjectmodel.rfanova.repl.co/webhook

```python
import requests
import time

def send_data():

    # URL of Flask application
    url = 'https://graciousjadedobjectmodel.rfanova.repl.co/webhook'

    # Example data 
    data = {
        'material': [
            {'name': 'Material1', 'cost': '100', 'units': '5'},
            {'name': 'Material2', 'cost': '150', 'units': '3'},
            {'name': 'Material2', 'cost': '150', 'units': '3'}
        ]
    }

    # POST request
    try:
        response = requests.post(url, json=data)
        print("Response from server:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
```

        
# Reciveing data
- In order to properly  send back the data i will need a webhook setup like below and your web app's URL

```python
# receiver.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received data:", data)
    return "Data received!"

```


