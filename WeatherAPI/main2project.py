from flask import Flask,render_template
import pandas as pd

filename = "dictionary.csv"
app = Flask('__name__')
df = pd.read_csv(filename)

@app.route('/')


def home():
    return render_template("home2project.html")

@app.route('/api/v1/<word>')
def about(word):
    definition = df.loc[df["word"] == word]["definition"].values[0]
    return {"definition":definition,"word":word}

if __name__ == '__main__':
    app.run(debug=True,port= 5002)