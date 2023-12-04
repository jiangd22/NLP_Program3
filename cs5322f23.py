import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import PunktSentenceTokenizer,sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

# Download nltk resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def readFile(filename):
# Read the file from the same directory as this file
    text = []
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            # Read each line of the file
            for line in file:
                # Remove the newline character
                line = line.strip()
                # Check if the line is not empty
                if line:
                    # Append the line to the list
                    text.append(line)
        return text
    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def setPreprocess(text):
# Preprocess the training set
    # Tokenize the text
    tokens = word_tokenize(text)
    # remove all punctuations
    tokens = [w for w in tokens if w.isalpha()]
    # Convert to lowercase
    tokens = [w.lower() for w in tokens]
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    return lemmatized_tokens

def wordnetSynsetsComparison(word1, word2):
    # wordnet synsets comparison
    try:
        # Get the synsets of the words
        synset1 = wordnet.synsets(word1) [0]
        synset2 = wordnet.synsets(word2) [0]
        if synset1.wup_similarity(synset2) is None:
            return 0
        else:
            return synset1.wup_similarity(synset2)

    except IndexError:
        # print(f"Error: Synset not found for {word1} or {word2}")
        return 0

    except Exception as e:
        # print(f"An error occurred: {e}")
        return 0
    except:
        return 0


def two_d_to_one_d(two_d_list):
    one_d_list = []
    for inner_list in two_d_list:
        for element in inner_list:
            one_d_list.append(element)
    return one_d_list

def synonymsCreator(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for i in syn.lemmas():
            synonyms.append(i.name())
    return synonyms

def testSetPreprocess(filename):
    sentence = filename
    testSet = readFile(sentence)
    # print(testSet)

    input = []
    for sentence in testSet:
        tokens = setPreprocess(sentence)
        input.append(tokens)
    # print(input)
    return input

def simlaryScore(list1, list2, testSet):
    output = []
    for sentence in testSet:
        first = []
        second = []
        for word in sentence:
            for word1 in list1:
                score1 = wordnetSynsetsComparison(word, word1)
                if score1 > 0.5:
                    first.append(score1)
            for word2 in list2:
                score2 = wordnetSynsetsComparison(word, word2)
                if score2 > 0.5:
                    second.append(score2)

        # average the score
        if len(first) != 0:
            firstScore = sum(first) / len(first)
        else:
            firstScore = 0
        if len(second) != 0:
            secondScore = sum(second) / len(second)
        else:
            secondScore = 0

        # compare the score
        if firstScore > secondScore:
            print("1")
            output.append("1")
        else:
            print("2")
            output.append("2")
    return output

def WSD_Test_Rubbish(list):
    # Read in training set
    sentence = "Data/rubbish.txt"
    trainSet = readFile(sentence)
    firstDef = []
    secondDef = []
    for sentence in trainSet:
        if sentence[0] == '1':
            if sentence[2] != ' ':
                firstDef.append(setPreprocess(sentence[3:]))
            else:
                firstDef.append(setPreprocess(sentence[2:]))
        else:
            if sentence[2] != ' ':
                secondDef.append(setPreprocess(sentence[3:]))
            else:
                secondDef.append(setPreprocess(sentence[2:]))
    firstDef = two_d_to_one_d(firstDef)
    secondDef = two_d_to_one_d(secondDef)

    input = []
    # Read in test set
    input = testSetPreprocess("Data/rubbish_test.txt")

    # Calculate similarity score
    list = simlaryScore(firstDef, secondDef, input)
    return list

def WSD_Test_Conviction(list):
    # Read in training set
    sentence = "Data/conviction.txt"
    trainSet = readFile(sentence)
    firstDef = []
    secondDef = []
    for sentence in trainSet:
        if sentence[0] == '1':
            if sentence[2] != ' ':
                firstDef.append(setPreprocess(sentence[3:]))
            else:
                firstDef.append(setPreprocess(sentence[2:]))
        else:
            if sentence[2] != ' ':
                secondDef.append(setPreprocess(sentence[3:]))
            else:
                secondDef.append(setPreprocess(sentence[2:]))
    firstDef = two_d_to_one_d(firstDef)
    secondDef = two_d_to_one_d(secondDef)

    input = []
    # Read in test set
    input = testSetPreprocess("Data/sample.txt")

    # Calculate similarity score
    list = simlaryScore(firstDef, secondDef, input)
    return list

def WSD_Test_Thorn(list):
    # Read in training set
    sentence = "Data/thorn.txt"
    trainSet = readFile(sentence)
    firstDef = []
    secondDef = []
    for sentence in trainSet:
        if sentence[0] == '1':
            if sentence[2] != ' ':
                firstDef.append(setPreprocess(sentence[3:]))
            else:
                firstDef.append(setPreprocess(sentence[2:]))
        else:
            if sentence[2] != ' ':
                secondDef.append(setPreprocess(sentence[3:]))
            else:
                secondDef.append(setPreprocess(sentence[2:]))
    firstDef = two_d_to_one_d(firstDef)
    secondDef = two_d_to_one_d(secondDef)

    input = []
    # Read in test set
    input = testSetPreprocess("Data/thorn_test.txt")

    # Calculate similarity score
    list = simlaryScore(firstDef, secondDef, input)
    return list


if __name__ == '__main__':
    listConviction = []
    listRubbish = []
    listThorn = []

    WSD_Test_Rubbish(listRubbish)
    # make a file named "result_<word>_<David_Jiang>.txt" and write to file
    file = open("Data/result_rubbish_name.txt", "w")
    for item in listRubbish:
        file.write(item + "\n")
    file.close()

    WSD_Test_Conviction(listConviction)
    # make a file named "result_<word>_<David_Jiang>.txt" and write to file
    file = open("Data/result_conviction_name.txt", "w")
    for item in listConviction:
        file.write(item + "\n")
    file.close()

    WSD_Test_Thorn(listThorn)
    # make a file named "result_<word>_<David_Jiang>.txt" and write to file
    file = open("Data/result_thorn_name.txt", "w")
    for item in listThorn:
        file.write(item + "\n")
    file.close()

