import numpy as np
from sklearn.linear_model import LinearRegression

# -------------------------------------------------
# Classical Machine Learning model for crop yield
# Algorithm: Linear Regression
# Purpose: Baseline model to compare against QML
# -------------------------------------------------

class CropYieldML:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        """
        X : feature matrix (n_samples, n_features)
        y : target yield values
        """
        self.model.fit(X, y)

    def predict(self, X):
        """
        X : feature matrix (usually shape (1, n_features))
        Returns: scalar float prediction
        """
        prediction = self.model.predict(X)

        # ✅ FIX: convert NumPy array → Python float
        return float(prediction[0])
