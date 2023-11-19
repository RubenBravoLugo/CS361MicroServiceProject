# CS361MicroServiceProject
Exampl UML Diagram: 

<img width="479" alt="image" src="https://github.com/RubenBravoLugo/CS361MicroServiceProject/assets/71678992/8325c7c9-b624-41fe-949b-aeb299c849cb">


### Requesting  
Requesting involves calling:  response = requests.post(url, json=data)
data is the jSON 
URL for the microservice is: https://graciousjadedobjectmodel.rfanova.repl.co/webhook
# Request Data.py
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

```python
# receiver.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received data:", data)
    return "Data received!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # Adjust the port if necessary
```


Example Recieving Data
