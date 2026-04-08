class CodeReviewTask:

    def __init__(self):
        self.data = [
            {
                "code": "password = '12345'",
                "issue": "security"
            },
            {
                "code": "for i in range(len(arr)): print(arr[i])",
                "issue": "performance"
            },
            {
                "code": "if x = 5: print(x)",
                "issue": "bug"
            }
        ]

    def get_data(self):
        return self.data

    def evaluate(self, predictions):
        correct = 0
        for pred, actual in zip(predictions, self.data):
            if pred == actual["issue"]:
                correct += 1

        return correct / len(self.data)