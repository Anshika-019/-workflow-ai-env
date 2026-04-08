def grade(predictions, data):
    correct = 0
    for pred, actual in zip(predictions, data):
        if pred == actual["label"]:
            correct += 1
    return correct / len(data)