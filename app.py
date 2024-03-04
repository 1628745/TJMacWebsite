from flask import Flask, render_template, request, send_file, send_from_directory

app = Flask(__name__)

@app.route('/')
def ask_questions():
    return render_template('index.html')


@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/page2')
def page2():
    return render_template('home.html')


@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')


@app.route('/page6')
def page6():
    return render_template('officerPage.html')


@app.route('/recommendations')
def recs():
    return render_template('recs.html')


@app.route('/EnviroFriendlyStocks')
def stocks():
    return render_template('stocks.html')


@app.route('/<folder>/<file>')
def file_finder(folder, file):
    return send_from_directory(folder, file)


@app.route('/<folder>/<folder2>/<file>')
def file_finder2(folder, folder2, file):
    directory = f"{folder}/{folder2}"
    return send_from_directory(directory, file)


app.debug = True
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
