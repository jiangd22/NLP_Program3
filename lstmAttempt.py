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

tf.random.set_seed(7)
top_words = 500
df = pd.read_csv("data/thorn.csv", sep=';')
print(df.head())
df.columns = df.columns.str.strip()
print("Column names:", df.columns)
X_train, X_test, y_train, y_test = train_test_split(df.get(["Text"]), df.get(["Label"]), test_size=0.2, random_state=42, shuffle=True)

# truncate and pad input sequences
max_review_length = 200
#X_train = sequence.pad_sequences(X_train, maxlen=max_review_length, dtype=object)
#X_test = sequence.pad_sequences(X_test, maxlen=max_review_length, dtype=object)
# create the model
embedding_vector_length = 32
model = Sequential()
model.add(Embedding(top_words, embedding_vector_length, input_length=max_review_length))
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