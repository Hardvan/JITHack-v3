from website import app
from flask import render_template, redirect, url_for, request
from website.forms import DataForm
import tensorflow as tf
import pandas as pd

age = -1
chol = -1
cp = -1


@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home_page():
    global age
    global chol
    global cp
    result = -1

    model = tf.keras.models.load_model(
        "Model/saved_model/my_model.h5")

    if request.method == "POST":
        data_form = dict(request.form)

        # For Personalised Dietary Plan
        age, chol, cp = int(data_form["age"]), int(
            data_form["chol"]), int(data_form["cp"])

        for i in data_form.copy():
            data_form[i] = float(data_form[i])

        # Converting the data into a dataframe
        df = pd.DataFrame([data_form])

        # Predicting the result
        result = model.predict(df)  # [[0.]] or [[1.]]
        result = int(result[0][0])
        print(result)

    return render_template('index.html', result=result)


@app.route('/blog')
def blog_page():
    global age
    global chol
    global cp
    age1 = age
    chol1 = chol
    cp1 = cp

    return render_template('here.html', age=age1, chol=chol1, cp=cp1)


@app.route('/about')
def about_page():
    return render_template('about.html')
