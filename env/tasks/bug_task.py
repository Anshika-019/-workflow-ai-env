class BugTask:

    def __init__(self):
        self.data = [
            {"text": "App crashes on login", "priority": "P0"},
            {"text": "UI misalignment on homepage", "priority": "P2"},
            {"text": "Payment gateway timeout", "priority": "P1"}
        ]

    def get_data(self):
        return self.data

    def evaluate(self, predictions):
        correct = 0
        for pred, actual in zip(predictions, self.data):
            if pred == actual["priority"]:
                correct += 1

        return correct / len(self.data)