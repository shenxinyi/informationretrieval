import numpy as np
import TextAnalysis

#
# Rocchio algorithm implementation
#
# Input: document-term matrix, relevance array
# Output: array sorted increasingly by weight
#

def Rocchio(matrix, relevances):
    for i in range(len(relevances)):
        relevance = relevances[i]
        if (relevance == 1):
            relevances[i] = 0.75
        elif (relevance == 0):
            relevances[i] = -0.15
    relevances.append(1)

    npMatrix = np.matrix(matrix)
    rVector = np.matrix(relevances)
    rocVector = (npMatrix * rVector.transpose()).A1
    srv = np.argsort(rocVector)[::-1]
    return srv

#
# Expand given query
#
# Input: query, document list, relevance array
# Output: term that will be added to query
#
def expand(query, documents, relevances):
    terms, matrix = TextAnalysis.createDocumentTermMatrix(documents)
    indices = Rocchio(matrix, relevances)
    newwords = []
    queryword = query.split(' ')
    for i in range(len(queryword)):
        queryword[i] = queryword[i].lower()

    for indice in indices:
        if (terms[indice].lower() in queryword):
            continue
        else:
            return terms[indice]
    return ''