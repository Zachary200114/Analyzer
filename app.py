from flask import Flask, render_template, request

app = Flask(__name__)

# Define a valid API key (in a real application, store securely)
VALID_API_KEY = "mysecretapikey"

def analyze_input(user_input):
    """
    A basic analysis function.
    Replace this with real logic for checking URLs or phishing emails.
    """
    if "phish" in user_input.lower():
        return "Suspicious – This input might be related to phishing."
    else:
        return "Seems safe – No obvious phishing signs found."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Retrieve the submitted API key and phishing input from the form
    api_key = request.form.get('apiKey', '')
    user_input = request.form.get('phishingInput', '')

    # Check the API key first
    if api_key != VALID_API_KEY:
        result = "Invalid API key provided. Please check your key and try again."
    else:
        result = analyze_input(user_input)

    # Render the analysis page with the results
    return render_template('analysis.html', result=result, user_input=user_input, api_key=api_key)

if __name__ == '__main__':
    app.run(debug=True)
