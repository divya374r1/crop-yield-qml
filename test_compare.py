import numpy as np
from utils.ml_model import CropYieldML
from utils.qml_model import CropYieldQML

# Same input features for fair comparison
X = np.array([[0.6, 0.24, 0.36, 0.0576]])
y_dummy = np.array([3.0])  # reference yield

# ML Model
ml_model = CropYieldML()
ml_model.train(X, y_dummy)
ml_pred = ml_model.predict(X)

# QML Model
qml_model = CropYieldQML()
qml_pred = qml_model.predict(X)

print("🔹 Classical ML Predicted Yield:", ml_pred)
print("🔹 Quantum ML Predicted Yield:", qml_pred)
