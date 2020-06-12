import string
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
text=open('read.txt',encoding='utf-8').read()
lowerCase=text.lower()
cleanText=lowerCase.translate(str.maketrans('','',string.punctuation))
tokenize_words=word_tokenize(cleanText,"english")
final_words=[]
for words in tokenize_words:
    if words not in stopwords.words('english'):
        final_words.append(words)
emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line=line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion=clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)  

print(emotion_list)
w= Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg > pos:
        print("Negative sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neaural Vibe")

sentiment_analyse(cleanText)

fig, ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
