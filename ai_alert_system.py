# ai_alert_system.py

class StudentPerformanceAnalyzer:

    def __init__(self, name, mid1, mid2):
        self.name = name
        self.mid1 = mid1
        self.mid2 = mid2

    def average_marks(self):
        return (self.mid1 + self.mid2) / 2

    def predict_risk(self):
        avg = self.average_marks()

        if self.mid1 < 20 and self.mid2 < 20:
            return "HIGH RISK"

        elif avg < 35:
            return "MEDIUM RISK"

        else:
            return "LOW RISK"

    def generate_alert(self):
        risk = self.predict_risk()

        if risk == "HIGH RISK":
            return f"""
ALERT FOR {self.name}

Student performance is critically low.
Immediate faculty intervention is recommended.
Parents should be informed.
Academic counseling is suggested.
"""

        elif risk == "MEDIUM RISK":
            return f"""
WARNING FOR {self.name}

Student performance needs improvement.
Additional practice and monitoring recommended.
"""

        else:
            return f"""
GOOD PERFORMANCE FOR {self.name}

Student is performing satisfactorily.
Keep up the good work.
"""

# Example Usage

student = StudentPerformanceAnalyzer(
    name="Jayaram",
    mid1=15,
    mid2=18
)

print("Average Marks:", student.average_marks())
print("Risk Level:", student.predict_risk())
print(student.generate_alert())