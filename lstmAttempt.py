# https://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/
# LSTM with Dropout for sequence classification in the IMDB dataset
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing import sequence
from datasets import load_dataset
import pandas as pd

# fix random seed for reproducibility
tf.random.set_seed(7)
# load the dataset but only keep the top n words, zero the rest
top_words = 5000

df = pd.read_csv("data/thorn.txt", sep='.', header=0, usecols= ['Label','Text'])
#dataFile = "thorn.csv"
#dataset = load_dataset("csv", data_files=dataFile)
print(df)
df_text_genre = df[['Label', 'Text']]
print(df_text_genre)
#(X_train, y_train), (X_test, y_test) = df.load_data(num_words=top_words)
X_train, X_test = train_test_split(df_text_genre, test_size=0.2, random_state=42, shuffle=True)
#(X_train, y_train), (X_test, y_test) = df
# truncate and pad input sequences
max_review_length = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
# create the model
embedding_vecor_length = 32
model = Sequential()
model.add(Embedding(top_words, embedding_vecor_length, input_length=max_review_length))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, epochs=3, batch_size=64)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))