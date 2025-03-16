class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        
        # Calcule la somme des longueurs des mots pondérés par les coefficients en utilisant zip
        total_length = sum(coef * len(word) for coef, word in zip(coefs, words))
        return total_length
    
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        
        # Calcule la somme des longueurs des mots pondérés par les coefficients en utilisant enumerate
        total_length = sum(coefs[i] * len(word) for i, word in enumerate(words))
        return total_length
