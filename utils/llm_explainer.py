# utils/llm_explainer.py

def explain_prediction(crop, temperature, rainfall, ml_yield, qml_yield, language="en"):
    """
    This function simulates LLM-style explanation.
    (Safe for offline demo & review)
    """

    explanations = {
        "en": f"""
For the selected crop ({crop}), the average temperature is {temperature}°C
and the rainfall is {rainfall} mm.

The classical Machine Learning model predicts a yield of {ml_yield:.2f}.
The Quantum Machine Learning model predicts a yield of {qml_yield:.2f}.

Quantum Machine Learning processes the data in a higher-dimensional space,
allowing it to capture complex relationships between climate and crop growth.
""",

        "hi": f"""
चयनित फसल ({crop}) के लिए औसत तापमान {temperature}°C है
और वर्षा {rainfall} मिमी है।

क्लासिकल मशीन लर्निंग मॉडल {ml_yield:.2f} उपज का अनुमान लगाता है।
क्वांटम मशीन लर्निंग मॉडल {qml_yield:.2f} उपज का अनुमान लगाता है।

क्वांटम मशीन लर्निंग उच्च-आयामी डेटा को बेहतर ढंग से संभाल सकती है।
""",

        "te": f"""
ఎంచుకున్న పంట ({crop}) కోసం సగటు ఉష్ణోగ్రత {temperature}°C
మరియు వర్షపాతం {rainfall} మి.మీ.

సాధారణ మెషిన్ లెర్నింగ్ మోడల్ {ml_yield:.2f} దిగుబడిని అంచనా వేస్తుంది.
క్వాంటం మెషిన్ లెర్నింగ్ మోడల్ {qml_yield:.2f} దిగుబడిని అంచనా వేస్తుంది.

క్వాంటం మెషిన్ లెర్నింగ్ సంక్లిష్ట డేటాను మెరుగుగా నిర్వహిస్తుంది.
""",

        "ta": f"""
தேர்ந்தெடுக்கப்பட்ட பயிர் ({crop}) க்கான சராசரி வெப்பநிலை {temperature}°C
மற்றும் மழைப்பொழிவு {rainfall} மிமீ.

பாரம்பரிய மெஷின் லேர்னிங் மாதிரி {ml_yield:.2f} விளைச்சலை கணிக்கிறது.
குவாண்டம் மெஷின் லேர்னிங் மாதிரி {qml_yield:.2f} விளைச்சலை கணிக்கிறது.
""",

        "kn": f"""
ಆಯ್ದ ಬೆಳೆ ({crop})ಗಾಗಿ ಸರಾಸರಿ ತಾಪಮಾನ {temperature}°C
ಮತ್ತು ಮಳೆಯ ಪ್ರಮಾಣ {rainfall} ಮಿಮೀ.

ಸಾಮಾನ್ಯ ಮೆಷಿನ್ ಲರ್ನಿಂಗ್ ಮಾದರಿ {ml_yield:.2f} ಇಳುವರಿಯನ್ನು ಅಂದಾಜಿಸುತ್ತದೆ.
ಕ್ವಾಂಟಂ ಮೆಷಿನ್ ಲರ್ನಿಂಗ್ ಮಾದರಿ {qml_yield:.2f} ಇಳುವರಿಯನ್ನು ಅಂದಾಜಿಸುತ್ತದೆ.
"""
    }

    return explanations.get(language, explanations["en"])
