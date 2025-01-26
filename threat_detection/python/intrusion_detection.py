from sklearn.ensemble import IsolationForest
import numpy as np

X = np.random.rand(100, 2)

X = np.vstack([X, np.array([[5, 5], [6, 6], [7, 7]])])

model = IsolationForest()
model.fit(X)

pred = model.predict(X)
print("Anomalies detected: ", np.where(pred == -1))
