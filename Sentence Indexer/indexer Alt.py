
# Program to index sentences



stopWords = [ "a", "i", "it", "am", "at", "on", "or", "in", "of", \
              "to", "is", "so", "too", "my", \
              "the", "and", "but", "are", "very", "here", "from", \
              "them", "then", "they", "than", "this", "that", \
              "though", "why", "yet", "has" ] 

noStemWords = [ "feed", "mass", "make", "rest", "ring", \
                "thing", "walrus", "wing", "wish" ]

stems = ["ing", "ish", "ly", "est", "ed", "es", "s"]

inptxt = open("inputtext.txt", "r")
punctuation = [".", ",", ":", ";", "!", "?", "&", "'", "-"]
dictionary = {}
LineList = []
n = 0
splitstring = []
innerstring = ''
for line in inptxt:
    LineList = LineList + [n]
    innerstring = line
    
    #for loop to remove punctuation by replacing them with nothing
    for i in punctuation:
        innerstring = innerstring.replace(i, '')
    innerstring = innerstring.lower()
    #print(innerstring)

    
    #Removes stopwords by converting string to a list and then checks word for word
    splitstring = innerstring.split()
    for word in stopWords:
        for word1 in splitstring:
            if word == word1:
                splitstring.remove(word)

                

    #Stemming
    #Improvement - try not using magic number, hint, store list and compare
    v = 0
    while v < 5:
        for word in splitstring:
            if word not in noStemWords:
                for s in stems:
                    if s in word[-len(s):]:
                        f = splitstring.index(word)
                        splitstring.pop(f)
                        word = word[:-len(s)]
                        splitstring.insert(f, word)
                        #print(word)
        v += 1
    #Creates dictionary with index         
    for word in splitstring:
        if word in dictionary:
            if dictionary[word][0] != n+1:
                dictionary[word] = dictionary[word] + [n+1]
        else:
            dictionary[word] = [n+1]


    #print(splitstring)
    innerstring = ' '.join(splitstring)
    #print(innerstring)
    
    n += 1



#Printing the index
print("the index is")
b = 0
for item in dictionary:
    if len(dictionary[item]) > b and len(dictionary[item]) != 0:
        print(item + " " + str(dictionary[item][0]) + ", " + str(dictionary[item][b+1]))
    else:
        print(item + " " + str(dictionary[item][0]))
    b += 1
#for item in dictionary:
    #print(item + " " + ','.join(str(x) for x in dictionary[item]))

#print(dictionary)
