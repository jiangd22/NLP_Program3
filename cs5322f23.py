
## where list is a list of string, each string is a sentence that contain the word “rubbish”.
# You should output a list of numbers, each number corresponds to the sense of the word
# “rubbish” for each sentence (either 1 or 2). Notice that you are responsible for the number
# to match with the corresponding sentence, and each number is either 1 or 2 (NOT 0 or 1)
import lesk
import re

TESTING = 0

# somehow every test file we were given is formatted slightly differently,
# so I'm doing the ugly but easy thing and making each file its own parse function.
# we won't need these for the input file that looks like sample.txt
def parseRubbish(file):
    definitions = []
    # parallel lists for senses and contexts to check accuracy 
    senses = []
    contexts = []
    with open(file) as f:
        regex1 = re.compile('\((.*?)\)', re.M) 
        for line in f.read().splitlines():
            d = regex1.findall(line)
            for item in d:
                if(item == 'n'):continue
                definitions.append(item)
            if(d == []):
                senses.append(line[0])
                contexts.append(line[2:])
    del contexts[0]
    del senses[0]
    return definitions, senses, contexts
def parseConviction(file):
    definitions = []
    # parallel lists for senses and contexts to check accuracy 
    senses = []
    contexts = []
    count = 0
    with open(file) as f:
        for line in f.read().splitlines():
            if(count == 0): 
                count += 1
                continue
            if(count == 1 or count == 2): 
                count += 1
                definitions.append(line[3:])
                continue
            senses.append(line[0])
            contexts.append(line[2:])
            count += 1
    print(definitions)
    return definitions, senses, contexts
def parseThorn(file):
    definitions = []
    # parallel lists for senses and contexts to check accuracy 
    senses = []
    contexts = []
    count = 0
    with open(file) as f:
        for line in f.read().splitlines():
            if(count == 0): 
                count += 1
                continue
            if(count == 1 or count == 2): 
                count += 1
                definitions.append(line[10:])
                continue
            senses.append(line[0])
            contexts.append(line[3:])
            count += 1
    print(definitions)
    return definitions, senses, contexts

def WSD_Test_Rubbish(l):    
    definitions, senses, contexts = parseRubbish("data/rubbish.txt")
    correct = 0
    total = len(contexts)
    if(TESTING): l = contexts
    simple_lesk = lesk.SimpleLesk()
    index = 0
    f = open("result_rubbish_calvertmaxwell.txt", "w")
    for context in l:
        sense = simple_lesk.lesk(context, "rubbish")
        answer = "1"
        if(sense.definition() == definitions[0]):
            answer = "1"
        else:
            answer = "2"
        f.write(answer+'\n')
        if(answer == senses[index] and TESTING): correct += 1
        if(TESTING): print("Context: ", context, "\nDefinition guess: ", definitions[int(answer)-1])
        if(TESTING): print("Guess: ", answer, "\tActual: ", senses[index])
        index += 1
    f.close()
    if(TESTING):return (correct/total)*100
    else:return

def WSD_Test_Conviction(l):
    definitions, senses, contexts = parseConviction("data/conviction.txt")
    correct = 0
    total = len(contexts)
    if(TESTING): l = contexts
    simple_lesk = lesk.SimpleLesk()
    index = 0
    f = open("result_conviction_calvertmaxwell.txt", "w")
    for context in l:
        sense = simple_lesk.lesk(context, "conviction")
        answer = "1"
        if(sense.definition() == definitions[0]):
            answer = "1"
        else:
            answer = "2"
        f.write(answer+'\n')
        if(answer == senses[index] and TESTING): correct += 1
        if(TESTING): print("Context: ", context, "\nDefinition guess: ", definitions[int(answer)-1])
        if(TESTING): print("Guess: ", answer, "\tActual: ", senses[index])
        index += 1
    f.close()
    if(TESTING):return (correct/total)*100
    else:return

def WSD_Test_Thorn(l):
    definitions, senses, contexts = parseThorn("data/thorn.txt")
    correct = 0
    total = len(contexts)
    if(TESTING): l = contexts
    simple_lesk = lesk.SimpleLesk()
    index = 0
    f = open("result_thorn_calvertmaxwell.txt", "w")
    for context in l:
        sense = simple_lesk.lesk(context, "thorn")
        answer = "1"
        if(sense.definition() == definitions[0]):
            answer = "1"
        else:
            answer = "2"
        f.write(answer+'\n')
        if(answer == senses[index] and TESTING): correct += 1
        if(TESTING): print("Context: ", context, "\nDefinition guess: ", definitions[int(answer)-1])
        if(TESTING): print("Guess: ", answer, "\tActual: ", senses[index])
        index += 1
    f.close()
    if(TESTING):return (correct/total)*100
    else:return

# insert files here at actual run
# order rubbish, conviction, thorn
files = []
contexts = [[],[],[]]
ind = 0
# for f in files:
    # with open("data/sample.txt") as file:
    #     for line in file:
    #         contexts[ind].append(line)
    # WSD_Test_Conviction(sample)
    # ind+=1
print(WSD_Test_Rubbish(contexts[0][0]))
print(WSD_Test_Conviction(contexts[1][0]))
print(WSD_Test_Thorn(contexts[2][0]))