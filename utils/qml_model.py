import pennylane as qml
import numpy as np

# ---------------- QML SETUP ---------------- #

# 4 qubits → supports higher-dimensional encoding
n_qubits = 4
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def quantum_circuit(features, weights):
    # Encode classical features into quantum states
    for i in range(n_qubits):
        qml.RY(features[i], wires=i)

    # Trainable quantum layer
    for i in range(n_qubits):
        qml.RY(weights[i], wires=i)

    # Measurement
    return qml.expval(qml.PauliZ(0))


# ---------------- QML MODEL ---------------- #

class CropYieldQML:
    def __init__(self):
        # Trainable parameters (simulated training)
        self.weights = np.random.uniform(0, np.pi, n_qubits)

    def predict(self, X):
        """
        X: shape (1, num_features)
        Returns: scalar float yield prediction
        """

        x = X[0]                      # take first sample
        x = np.pad(
            x,
            (0, max(0, n_qubits - len(x))),
            mode="constant"
        )

        prediction = quantum_circuit(x, self.weights)

        # ✅ CRITICAL FIX: convert to Python float
        return float(prediction)
