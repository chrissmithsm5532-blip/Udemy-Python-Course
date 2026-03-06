from flask import Flask,render_template

app = Flask('__name__')

@app.route('/')
def home():
    return render_template("home2project.html")

@app.route('/api/v1/<word>')
def about(word):
    #  df = pandas.read.csv("")
    #  temperature = df.station(date)
    return {"definition":word.upper(),"word":word}
    #{"station":station,"date":date,"temperature":temperature}

if __name__ == '__main__':
    app.run(debug=True,port= 5002)