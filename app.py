from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="codinginasnjnda"
@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/submission', methods=['POST'])
def Submit_form():
    for value in request.form:
        session[value]=request.form[value]
    return redirect('/result')

@app.route('/result')
def dsplay_results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)