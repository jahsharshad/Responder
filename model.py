# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
import joblib
# import matplotlib.pyplot as plt


# def train_model():
#     data = pd.read_csv("ResponseTimes.csv")
#
#     X = data[["EmergencyStations", "Area", "Urban"]]
#     Y = data[["ResponseTime"]]
#
#     Y = Y.to_numpy()
#     Y = Y.flatten()
#
#     clf = RandomForestRegressor()
#     clf.fit(X, Y)
#
#     predicted = clf.predict(X)
#
#     avg=0
#     for i in range(len(predicted)-1):
#         avg = avg + abs(predicted[i] - Y[[i]])
#         print(avg)
#
#     print("Loss: ", avg/len(predicted))
#
#     ans = input("Save?")
#     if ans == "y":
#         filename = 'model.sav'
#         joblib.dump(clf, "./random_forest.joblib")


def predict(stations, area, urban):
    clf = joblib.load("./random_forest.joblib")
    prediction = clf.predict([[stations, area, urban]])
    prediction = prediction.flatten()
    return prediction[0].item()

'''print(predict(429,789,0.5))
print(type(predict(429,789,0.5)))'''
