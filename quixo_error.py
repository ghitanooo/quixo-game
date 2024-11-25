class QuixoError(Exception):
    """
    Classe d'exception personnalisée pour les erreurs liées au jeu Quixo.
    """
    def __str__(self):
        """
        Retourne une représentation lisible de l'exception avec son message.
        """
        f"QuixoError: {self.args[0]}"
        return "QuixoError"