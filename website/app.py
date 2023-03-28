from flask import Flask, render_template, request
import pandas as pd
import tensorflow as tf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'


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

    model = tf.keras.models.load_model("./my_model.h5")

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

    return render_template("index.html", result=result)


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


if __name__ == '__main__':
    app.run(debug=True)

# Setup:
# ? set FLASK_APP=app.py
# ? Run the app.py file
