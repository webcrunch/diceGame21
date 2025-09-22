import os.path


class ScoreManager:
    def __init__(self, filename="scores.txt"):
        self.filename = filename

    def load_scores(self):
        scores = {"player_wins": 0, "dealer_wins": 0}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    try:
                        key, value = line.strip().split(":")
                        scores[key] = int(value)
                    except (ValueError, IndexError):
                        continue
        return scores

    def save_scores(self, scores):
        with open(self.filename, "w") as file:
            for key, value in scores.items():
                file.write(f"{key}:{value}\n")
