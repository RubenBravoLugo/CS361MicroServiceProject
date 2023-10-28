from flask import Flask, request, redirect

app = Flask(__name__)





@app.route('/')
def index():
    return redirect('https://websote.rfanova.repl.co', code=302) 



@app.route('/process', methods=['GET', 'POST'])
def process_data():
    if request.method == 'POST':
        number = request.form.get('number')  
        word = request.form.get('word')  # Getting the word from  form

        print(f"Form data: {request.form}")  

        response_text = ""  


      

        if number and number.isdigit():
            result = int(number) + 1
            response_text += f"The new number is: {result}<br>"
        else:
            response_text += "Invalid input for number. Please enter a valid number.<br>"



      
        if word:  # Cword entered
            response_text += f"The received word is: {word}<br>"
        else:
            response_text += "No word entered.<br>"

        return response_text 
    else:
        return redirect('https://websote.rfanova.repl.co', code=302) 





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)  