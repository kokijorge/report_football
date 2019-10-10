from afinn import Afinn
afinn = Afinn(language="en")
score = afinn.score('goal');
print(score);