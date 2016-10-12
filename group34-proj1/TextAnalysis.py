import math

#
# Create Inverted Index
#
# Input: document list
# Output: Dictionary {term:{doc:tf}}
#
def createInvertedIndex(documents):
    f = open('stop.txt', 'r')
    stopwords = f.readlines()
    stopwords_s = [i.rstrip('\n') for i in stopwords]
    invertedIndex = {}
    for itera in range(len(documents)):
        document = documents[itera]
        for word in document:
            word = word.lower()
            if word in stopwords_s or word == '' or word == ' ':
                continue
            if word in invertedIndex:
                if itera in invertedIndex[word]:
                    invertedIndex[word][itera] = invertedIndex[word][itera] + 1
                else:
                    invertedIndex[word][itera] = 1
            else:
                invertedIndex[word] = {itera: 1}
    f.close()
    return invertedIndex

#
# Create Document-term matrix
#
# Input: document list
# Output: document-term matrix(#term * #doc)
#
def createDocumentTermMatrix(documents):
    invertedIndex = createInvertedIndex(documents)
    terms = invertedIndex.keys()
    matrix = [[0 for x in range(11)] for y in range(len(terms))]
    for i in range(len(terms)):
        term = terms[i]
        idf = math.log(10.0 / len(invertedIndex[term]))
        for j in range(11):
            if j in invertedIndex[term]:
                tf = 1.0 * invertedIndex[term][j] / len(documents[j])
                matrix[i][j] = tf * idf
    return terms, matrix