# CS361MicroServiceProject
Exampl UML Diagram: 

<img width="476" alt="image" src="https://github.com/RubenBravoLugo/CS361MicroServiceProject/assets/71678992/ab432d4c-0785-4739-9c84-f70f87f37777">

This will create a code block formatted specifically for Python code.

### Adding a Title to Code Blocks

You can also add a title or a filename to your code blocks for better readability. While this is not standard Markdown, GitHub supports this feature.

Example:
```markdown
```python:title=hello_world.py
def hello_world():
    print("Hello, World!")

# Request Data.py
```python
import requests
import time

def send_data():
    # URL of the Flask application
    url = 'https://graciousjadedobjectmodel.rfanova.repl.co/webhook'
    # Example data to send
    data = {
        'material': [
            {'name': 'Material1', 'cost': '100', 'units': '5'},
            {'name': 'Material2', 'cost': '150', 'units': '3'},
            {'name': 'Material2', 'cost': '150', 'units': '3'}
        ]
    }
    # Making a POST request
    try:
        response = requests.post(url, json=data)
        print("Response from server:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
'''




        
# Reciveing data
send_data()


Example Recieving Data
