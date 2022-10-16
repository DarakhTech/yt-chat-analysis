TRAIN_FILE = './data/sst_train.txt'

class FastTextSentiment():
    """Predict fine-grained sentiment scores using FastText"""
    def __init__(self, model_file: str=None) -> None:
        import fasttext
        self.model = fasttext.load_model(model_file)

    def score(self, text: str) -> int:
        # Predict just the top label (hence 1 index below)
        labels, probabilities = self.model.predict(text, 1)
        pred = int(labels[0][-1])
        return pred

    def predict(self, sentence: None, lower_case: bool):
        return self.score(sentence)

ft = FastTextSentiment('./model/sst5.ftz')