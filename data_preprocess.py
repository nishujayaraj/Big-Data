import pandas as pd
import numpy as np
import matplotlib
import inline
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'

from bs4 import BeautifulSoup
import re
from nltk.tokenize import WordPunctTokenizer
tok = WordPunctTokenizer()

pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))

def tweet_cleaner(text):
    soup = BeautifulSoup(text,"html.parser")
    souped = soup.get_text()
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z]", " ", clean)
    lower_case = letters_only.lower()

    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()

df1 = pd.read_csv(r"OutputStreaming.csv",error_bad_lines=False,names=["text"],delimiter=';')
#selectedC=df1[["text"]]
new_df = df1.copy()
new_df.head()
testing = df1.text[:10]
print(testing)

test_result = []
for t in testing:
    test_result.append(tweet_cleaner(t))
print(test_result)
c_df = pd.DataFrame(test_result,columns=['text'])
c_df.head()
c_df.to_csv("testtweet.csv",encoding='utf-8')
