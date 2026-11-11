from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('registration.html')
@app.route('/success', methods=['POST'])
def success():
    name = request.form['name']
    id=request.form.get('id')
    year=request.form.get('year')
    return render_template('success.html', name=name, id=id, year=year)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
