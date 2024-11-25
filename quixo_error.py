class QuixoError(Exception):
    def __str__(self):
        if self.args and self.args[0]:
            f"QuixoError: {self.args[0]}"
        return "QuixoError"