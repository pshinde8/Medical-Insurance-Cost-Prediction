from pyexpat import model
from unicodedata import name
from flask import Flask, render_template, request
import numpy as np
import pickle

app=Flask(__name__)

model = pickle.load(open("rf_reg.pkl","rb"))

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/sub',methods=['POST'])
def submit():
    if request.method=="POST":
        features=[int(x) for x in request.form.values()]
        print(features)

        final=np.array(features).reshape((1,6))
        print(final)

        pred=model.predict(final)[0]
        print(pred)

        if pred < 0:
            return render_template('sub.html', pred="Error Calculating Amount!")
        else:
            return render_template("sub.html", pred="{0:.1f}".format(pred))

    return render_template("sub.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

