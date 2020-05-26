class Evaluator():
    """docstring for Evaluator."""

    def zip_evaluate(coefs, words):
        res = 0
        if (isinstance(coefs, list) and isinstance(words, list)
           and len(coefs) == len(words)):
            for z in tuple(zip(coefs, words)):
                if not isinstance(z[0], float) or not isinstance(z[1], str):
                    return -1
                res += z[0] * len(z[1])
            return res
        else:
            return -1

    def enumerate_evaluate(coefs, words):
        res = 0
        if (isinstance(coefs, list) and isinstance(words, list)
           and len(coefs) == len(words)):
            for c, z0 in enumerate(coefs):
                for d, z1 in enumerate(words):
                    if d == c:
                        if (not isinstance(z0, float)
                           or not isinstance(z1, str)):
                            return -1
                        res += z0 * len(z1)
            return res
        else:
            return -1


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print(Evaluator.zip_evaluate(coefs, words))
print(Evaluator.enumerate_evaluate(coefs, words))
