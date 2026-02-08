from utils.feature_engineering import build_feature_vector

sample_data = {
    "temperature": 30,
    "rainfall": 120,
    "crop": "Rice",
    "state": "Karnataka"
}

features = build_feature_vector(sample_data)

print("Feature Vector:")
print(features)
print("Feature Dimension:", features.shape)
