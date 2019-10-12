import io
import sys
import json

from os import listdir
from os.path import join

from afinn import Afinn
afinn = Afinn(language="en")
score = afinn.score('excellent');
print(score);