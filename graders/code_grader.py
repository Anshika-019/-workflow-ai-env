from graders.code_grader import grade

def evaluate(self, predictions):
    return grade(predictions, self.data)