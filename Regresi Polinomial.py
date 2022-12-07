from sklearn.preprocessing import polynomialFeatures
from sklearn import linear_model
import numpy as np

#Database
# X = Data, y = Target
x = [[1],[3],[5],[7],[9],[11],[13],[15],[17],[21]]
y = [1, 9, 17, 19, 25, 49, 81, 91, 101]

#Data uji
predict = np.array([[11]])
poly = polynomialFeatures(degree=2)
x_= poly.fiy_transform(x)
predict = poly.fit_transform(predict)
regr = linear_model.LinearRegression()
regr.fit(x_,y)

#Menampilkan data prediksi
print ("Prediksi")
print ("Input = ",predict)
print ("Output = ",regr.predict(predict_))
