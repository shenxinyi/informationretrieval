# informationretrieval
a) Project 1 Group 34
    group member1: Xinyi Shen xs2259
    group member2: Fei Peng fp2358

b)The files submitted contains:
	python files:
		BingQuery.py
		QueryExpansion.py
		TextAnalysis.py
	text file:
		stopword.txt
	transcript:
		transcript.txt
	readme:
		README.md

c) To run the code:
	In the commanndline, input:
	python BingQuery.py <query> <precision> <accountkey>

d) Internal Design:
    Start from getting user input query, bing account key, and precision.
    Get the top ten results from bing web search engine.
    Show each result to the user and record their feedback.
    If precision is not reached, the query-modification method is called
    We separate the code into three files, BingQuery.py is the main script.
    QueryExpansion.py is called if new query is needed, to get the new terms TextAnalysis.py is called to form the matrix that will be used in QueryExpansion.py.

e) Query-modification method:
    If the precision is not reached, the query-modification method is called.
    Step 0 is getting the users feedback and save it in the form of matrix consisting 1(relevance),0(non-relevance)--relevance matrix.
    Step 1, an inverted index file for all the terms in all documents(summaries returned) except the stopwords is structured.
    Step 2, having the inverted index file the matrix consist of the tfidf values for each term and each document is calculated.
    Step 3, take the tfisf matrix and relevance matrix as input, by using rocchio's equation, the top relevance term's index is obtained.
    Modified the query with the one new term and do the query again until the precision is reached.

f) Bing Search Account Key: Cpmz59giIw48cb4zHyVjiTOvmHeDJOh6DoZ9C6kzSQI


