import numpy as np
from utils.ml_model import CropYieldML

# Training data
X_train = np.array([
    [25, 120, 0.6, 0.2, 0.5, 1],
    [30, 80, 0.4, 0.3, 0.6, 0],
    [22, 150, 0.7, 0.1, 0.4, 1],
    [28, 90, 0.5, 0.25, 0.55, 0]
])

y_train = np.array([3.2, 2.1, 3.8, 2.5])

model = CropYieldML()
model.train(X_train, y_train)

# Feature vector from Phase 3.3
X_test = np.array([[26, 110, 0.6, 0.2, 0.5, 1]])

prediction = model.predict(X_test)

print("ML Predicted Yield:", prediction)
