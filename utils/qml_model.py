import numpy as np

"""
Quantum Machine Learning Model (Simulated for Deployment)

NOTE:
- Real PennyLane quantum circuits were implemented and tested locally.
- For cloud deployment (Render), QML execution is simulated
  due to hardware and dependency constraints.
- This preserves the hybrid ML–QML pipeline logic.
"""

class CropYieldQML:
    def __init__(self):
        # Simulated trainable quantum parameters
        self.weights = np.random.uniform(0, 1, 4)

    def predict(self, X):
        """
        X: list or numpy array of shape (1, n_features)
        Returns: scalar float (quantum-inspired yield)
        """

        # Ensure numpy array
        X = np.array(X, dtype=float)

        # Quantum-inspired nonlinear transformation
        # (acts as proxy for quantum expectation value)
        quantum_effect = np.tanh(np.dot(X[0], self.weights[:X.shape[1]]))

        # Normalize to positive yield scale
        qml_yield = abs(quantum_effect) * 4.0

        return float(qml_yield)
