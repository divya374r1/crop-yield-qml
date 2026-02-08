import numpy as np
from utils.qml_model import CropYieldQML

# Same feature vector used for ML
X = np.array([[0.6, 0.24, 0.36, 0.0576]])

qml_model = CropYieldQML()
prediction = qml_model.predict(X)

print("QML Predicted Yield:", prediction)
