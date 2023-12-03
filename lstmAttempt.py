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

# Read the file from the same directory as this file
def readFile(filename):
    text = []
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            # Read each line of the file
            for line in file:
                # Remove the newline character
                line = line.strip()
                # Check if the line is not empty
                if line:
                    # Replace spaces with ';'
                    line = line.replace(' ', ';')
                    # Check the length of the line
                    if len(line) < 500:
                        # Add padding if it's under 500 characters
                        padding_length = 500 - len(line)
                        line = line + '0' * padding_length
                    elif len(line) > 500:
                        # Truncate the line if it's over 500 characters
                        line = line[:500]
                    # Append the modified line to the list
                    text.append(line)
        return text
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == '__main__':
    # fix random seed for reproducibility
    tf.random.set_seed(7)
    # load the dataset but only keep the top n words, zero the rest
    top_words = 5000

    df = pd.read_csv("data/conviction.txt", sep='.', header=0, usecols= ['Label','Text'])
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