import joblib

def predict(stations, area, urban):
    clf = joblib.load("./random_forest.joblib")
    prediction = clf.predict([[stations, area, urban]])
    prediction = prediction.flatten()
    return prediction[0].item()

'''print(predict(429,789,0.5))
print(type(predict(429,789,0.5)))'''
