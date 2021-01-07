# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:35:40 2020

@author: Teena Saj
"""
''' .txt FILE SUMMARIZER'''
def textfilesummary(raw_text):
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    import heapq
    
    file = open(raw_text, "r")
    filedata = file.read()
    
    stopWords = set(stopwords.words("english"))
    word_frequencies = {}
    for word in nltk.word_tokenize(filedata):
        if word not in stopWords:
	        if word not in word_frequencies.keys():
	            word_frequencies[word] = 1
	        else:
	            word_frequencies[word] += 1
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_list = nltk.sent_tokenize(filedata)
    sentence_scores = {}
    for sent in sentence_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_frequencies.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in sentence_scores.keys():
	                    sentence_scores[sent] = word_frequencies[word]
	                else:
	                    sentence_scores[sent] += word_frequencies[word]
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)  
    return summary
    









'''WEBSITE SUMMARIZER'''

def websitesummary(link):

    import bs4 as bs
    import urllib.request
    import re
    import nltk
    scraped_data = urllib.request.urlopen(link)
    
    article = scraped_data.read()
    
    parsed_article = bs.BeautifulSoup(article,'lxml')
    
    paragraphs = parsed_article.find_all('p')
    
    article_text = ""
    
    for p in paragraphs:
        article_text += p.text
    # Removing Square Brackets and Extra Spaces
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    # Removing special characters and digits
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
    sentence_list = nltk.sent_tokenize(article_text)
    stopwords = nltk.corpus.stopwords.words('english')
    
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
                
    maximum_frequncy = max(word_frequencies.values())
    
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    import heapq
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    
    summary = ' '.join(summary_sentences)
    print(summary)










'''RAW TEXT SUMMARIZER'''  
def rawtextsummary(raw_text):
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    import heapq
    stopWords = set(stopwords.words("english"))
    word_frequencies = {}
    for word in nltk.word_tokenize(raw_text):
        if word not in stopWords:
	        if word not in word_frequencies.keys():
	            word_frequencies[word] = 1
	        else:
	            word_frequencies[word] += 1
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_list = nltk.sent_tokenize(raw_text)
    sentence_scores = {}
    for sent in sentence_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_frequencies.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in sentence_scores.keys():
	                    sentence_scores[sent] = word_frequencies[word]
	                else:
	                    sentence_scores[sent] += word_frequencies[word]
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)  
    return summary











'''NEWS ARTICLE SUMMARIZER'''
def newssummary(url):
    from newspaper import Article 
    #For different language newspaper refer above table 
    toi_article = Article(url, language="en") # en for English 
    
    #To download the article 
    toi_article.download() 
    
    #To parse the article 
    toi_article.parse() 
    
    #To perform natural language processing ie..nlp 
    toi_article.nlp() 
    
    #To extract title 
    print("Article's Title:") 
    print(toi_article.title) 
    print("n") 
    
    #To extract text 
    #print("Article's Text:") 
    #print(toi_article.text) 
    #print("n") 
    
    #To extract summary 
    print("Article's Summary:") 
    print(toi_article.summary) 
    print("n") 
    
    #To extract keywords 
    #print("Article's Keywords:") 
    #print(toi_article.keywords) 











