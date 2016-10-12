import sys
import urllib2
import base64
import json
import re
import QueryExpansion

query = sys.argv[1]
precision = float(sys.argv[2])
accountKey = sys.argv[3]

#
# Get relevant feedback from user
#
# Input: result returned by Bing
# Output:
#       relevance: array that indicates whether ith doc is relevant
#       count: number of relevant documents
#
def checkRelevance(bingresult,file):
    relevance = []
    count = 0
    for itera in range(len(result)):
        geturl = result[itera]['Url']
        gettitle = result[itera]['Title']
        getsummary = result[itera]['Description']


        print '\nResult ' + str(itera + 1)
        print '['
        print 'URL: ' + geturl
        print 'Title: ' + gettitle
        print 'Summary: ' + getsummary
        print ']'

        file.write('\nResult ' + str(itera + 1)+'\n')

        user_input = raw_input("Relevant (Y/N)? ").upper()
        while (user_input != 'Y' and user_input != 'N'):
            user_input = raw_input("Relevant (Y/N)? Input 'Y' OR 'N'").upper()
        if user_input == 'Y':
            count = count + 1
            print 'Result ' + str(itera + 1) + " is valid! " + str(count) + " valid results so far."
            file.write('\nRelevant: YES\n')
            relevance.append(1)
        else:
            relevance.append(0)
            file.write('Relevant: NO\n')
            print 'Result ' + str(itera + 1) + " is not valid!" + str(count) + " valid results so far."
        file.write('[\n')
        file.write('URL: ' + geturl+'\n')
        file.write('Title: ' + gettitle.encode("utf-8")+'\n')
        file.write('Summary: ' + getsummary.encode("utf-8")+'\n')
        file.write(']\n')

    return relevance, count

#
# Extract summary texts from Bing result
#
# Input: result returned by Bing
# Output: a list of summary text
#
def getSummaries(bingresult):
    summaries = []
    for itera in range(len(bingresult)):
        summary = bingresult[itera]['Description']
        summary = re.sub(r'[^a-zA-Z0-9 ]', '', summary)
        summaries.append(summary.split(' '))
    return summaries


#
# Main process
#
f=open('transcript.txt','ab')
round=0
condition = True
while condition:
    round=round+1
    f.write("\nROUND "+str(round)+'\n')
    f.write("QUERY "+query+'\n')
    bingUrl = 'https://api.datamarket.azure.com/Bing/Search/Web?Query=%27' + urllib2.quote(
        query) + '%27&$top=10&$format=json'
    accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
    headers = {'Authorization': 'Basic ' + accountKeyEnc}
    req = urllib2.Request(bingUrl, headers=headers)
    response = urllib2.urlopen(req)
    content = response.read()
    ddata = json.loads(content)
    dddata = ddata['d']
    result = dddata['results']
    if (len(result) == 0):
        print "No result!"
        break

    relevance, count = checkRelevance(result,f)
    if (count >= precision*10):
        f.write('\nprecision: ' + str(1.0 * count / 10))
        break
    elif count==0:
        f.write('\nprecision: ' + str(1.0 * count / 10))
        f.write('\nNo relevant result, query stoped')
        break
    f.write('\nprecision: ' + str(1.0 * count / 10)+'\n')
    documents = getSummaries(result)
    documents.append(query)
    term = QueryExpansion.expand(query, documents, relevance)
    query = query + " " + term
    print 'The new query is ', query