from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from tensorflow import keras

from Alloy.models import User_Detail
# Required modules

import numpy as np
import pandas as pd
import tensorflow as tf

# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# from matplotlib import pyplot as plt


# Create your views here.
def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        purpose = request.POST['purpose']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('/signup/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('/signup/')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                )
                user_detail = User_Detail(user=user, purpose=purpose)
                user.save()
                user_detail.save()
                print('user created')
                return redirect('/')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/')

    else:
        return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username')
            return redirect('/')

    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def output(request):
    out = ""
    if request.method == "POST":
        carbon = request.POST['Carbon']
        silicon = request.POST['Silicon']
        manganese = request.POST['Manganese']
        phosphorus = request.POST['Phosphorus']
        nickel = request.POST['Nickel']
        chromium = request.POST['Chromium']
        molybdenum = request.POST['Molybdenum']
        manganese_sulfur = request.POST['Molybdenum_Sulfur']
        cooling_rate = request.POST['Cooling_Rate']
        tempering_temperature = request.POST['Tempering_Temperature']

        # print("Carbon: " + carbon + ", Silicon: "
        #       + silicon + ", Mangnese: " + manganese + ", Phosphorus: "
        #       + phosphorus + ", Nickel: " + nickel + ", Chromium: "
        #       + chromium + ", Molybdenum: " + molybdenum + ", Manganese/Sulfur: "
        #       + manganese_sulfur + ", Cooling Rate: " + cooling_rate + ", Tempering Temperature: "
        #       + tempering_temperature)

        # out = "Carbon: " + carbon + ", Silicon: " + silicon + ", Mangnese: " + manganese + ", Phosphorus: " + phosphorus + ", Nickel: " + nickel + ", Chromium: " + chromium + ", Molybdenum: " + molybdenum + ", Manganese/Sulfur: " + manganese_sulfur + ", Cooling Rate: " + cooling_rate + ", Tempering Temperature: " + tempering_temperature
        # messages.success(request, out)

        input = np.array([[carbon, silicon, manganese, phosphorus, nickel, chromium, molybdenum, manganese_sulfur, cooling_rate, tempering_temperature]])
        # messages.success(request, input)
        output = runModel(input)
        print(output)
        # pd.DataFrame(columns=['YS', 'UTS', 'EL', 'RA', 'IS'], data=output)
        converted_list = [str(element) for element in output.flatten()]
        joined_string = ",".join(converted_list)
        print(joined_string)
        messages.info(request, joined_string)

    return redirect("/main/")

def runModel(input_array):
    data = pd.read_csv("Appendix 2 EN Steels.csv")
    X = data[['C', 'Si', 'Mn', 'P', 'Ni', 'Cr', 'Mo', 'Mn/S', 'CR', 'TT']]
    Y = data[['YS', 'UTS', 'EL', 'RA', 'IS']]
    # Scaling the data

    X_scale = MinMaxScaler()
    y_scale = MinMaxScaler()

    X_scaled = X_scale.fit_transform(X)
    y_scaled = y_scale.fit_transform(Y)

    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(10, activation='sigmoid'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(11, activation='sigmoid'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(11, activation='sigmoid'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(5, activation='linear')
    ])

    # Custom loss

    def rmse(y_true, y_pred):
        return tf.math.sqrt(tf.keras.losses.mean_squared_error(y_true, y_pred))

    optim2l = tf.keras.optimizers.SGD(learning_rate=0.55, momentum=0.65)
    loss = tf.keras.losses.mean_squared_error

    # compile model using mse as a measure of model2L performance

    model.compile(optimizer=optim2l, loss=loss, metrics=[rmse])

    input_scale = MinMaxScaler()

    input_scaled = input_scale.fit_transform(input_array)

    model.fit(X_scaled, y_scaled, epochs=10)
    # loading the model double layer

    model.load_weights('model2L.h5')
    # model = keras.models.load_model('model2L.hdf5')
    # print(model.summay())
    output_predicted = model.predict(input_scaled)
    # pd.DataFrame(columns=['YS', 'UTS', 'EL', 'RA', 'IS'], data=output_predicted)

    out = y_scale.inverse_transform(output_predicted)

    return out