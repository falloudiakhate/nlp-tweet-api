import django.db
from tensorflow import keras
import pandas as pd
# from keras.preprocessing.sequence import pad_sequences
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer




def predictClass(input):
  tokenizer = Tokenizer()
  data = {'tweet': [input]} 
  dframe = pd.DataFrame(data) 
  tokenizer.fit_on_texts(dframe.tweet)
  word_index = tokenizer.word_index
  vocab_size = len(tokenizer.word_index) + 1
  x = pad_sequences(tokenizer.texts_to_sequences(dframe.tweet),maxlen = 30) 
  model = keras.models.load_model('/home/falloudiakhate/Desktop/Freelence/nlp-tweet-api/Api/model.h5')
  y = model.predict(x)
  if(y > 0.5):
    return "SENTIMENT POSITIF"
  return " SENTMENT NEGATIF"
