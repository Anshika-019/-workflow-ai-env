from graders.email_grader import grade
class EmailTask:

    def __init__(self):
        self.data = [
            {"text": "Urgent: Server down", "label": "urgent"},
            {"text": "Win a lottery now", "label": "spam"},
            {"text": "Meeting at 5 PM", "label": "normal"}
        ]

    def get_data(self):
        return self.data



    def evaluate(self, predictions):
      return grade(predictions, self.data)