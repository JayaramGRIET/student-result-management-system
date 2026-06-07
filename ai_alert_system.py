from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Training Data
X = np.array([
    [15, 18],
    [12, 10],
    [25, 28],
    [35, 40],
    [45, 50],
    [55, 60],
    [18, 15],
    [42, 38]
])

y = np.array([
    "High Risk",
    "High Risk",
    "Medium Risk",
    "Medium Risk",
    "Low Risk",
    "Low Risk",
    "High Risk",
    "Low Risk"
])

model = DecisionTreeClassifier()
model.fit(X, y)

def generate_alert(name, mid1, mid2):
    prediction = model.predict([[mid1, mid2]])[0]

    if prediction == "High Risk":
        return f"{name}: Immediate faculty attention required."

    elif prediction == "Medium Risk":
        return f"{name}: Student needs improvement."

    return f"{name}: Student performance is satisfactory."
