from flask import Flask, render_template,request
from googlesearch import search
from libs.utilities import fetch_url_content,get_search_results

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('search') 
    print(f"User Input: {user_input}")
    
    for r in get_search_results(f'{user_input} prices',5):
        print("--------------------------------------")
        print()
        print(fetch_url_content(r))
        print()
        print("--------------------------------------")


    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)
