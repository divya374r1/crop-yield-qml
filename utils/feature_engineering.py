"""
PHASE 3.3 — FEATURE ENGINEERING

Purpose:
Convert raw agricultural + climate inputs into a
numerical feature vector suitable for ML and QML.

Why this matters:
• ML models require numeric vectors
• QML requires normalized, fixed-dimension inputs
• This step creates HIGH-DIMENSIONAL structured data
"""

import numpy as np

# --- Encoding dictionaries ---
CROP_ENCODING = {
    "Rice": 0.1,
    "Wheat": 0.2,
    "Maize": 0.3,
    "Millets": 0.4,
    "Sorghum": 0.5,
    "Pulses": 0.6,
    "Cotton": 0.7,
    "Sugarcane": 0.8,
    "Other": 0.9
}

STATE_ENCODING = {
    "Karnataka": 0.1,
    "Tamil Nadu": 0.2,
    "Andhra Pradesh": 0.3,
    "Telangana": 0.4,
    "Maharashtra": 0.5,
    "Other": 0.9
}

def build_feature_vector(data: dict):
    """
    Input:
        data = {
            'temperature': float (°C),
            'rainfall': float (mm),
            'crop': string,
            'state': string
        }

    Output:
        numpy array (feature vector)
    """

    temperature = float(data.get("temperature", 0)) / 50.0
    rainfall = float(data.get("rainfall", 0)) / 500.0

    crop_val = CROP_ENCODING.get(data.get("crop"), 0.9)
    state_val = STATE_ENCODING.get(data.get("state"), 0.9)

    # Polynomial expansion → NON-LINEAR FEATURES
    temp_sq = temperature ** 2
    rain_sq = rainfall ** 2

    # Final feature vector (HIGH-DIMENSIONAL)
    feature_vector = np.array([
        temperature,
        rainfall,
        temp_sq,
        rain_sq,
        crop_val,
        state_val
    ])

    return feature_vector
