#Final Python Code for NUTSHELL

from flask import Flask,render_template,url_for,request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
import bs4 as bs
import urllib.request
import re

app = Flask(__name__)

def rawtextsummary(raw_text):
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


def websitesummary(link):
	scraped_data = urllib.request.urlopen(link)
	article = scraped_data.read()
	parsed_article = bs.BeautifulSoup(article,'lxml')
	paragraphs = parsed_article.find_all('p')
	article_text = ""
	for p in paragraphs:
		article_text += p.text
	article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
	article_text = re.sub(r'\s+', ' ', article_text)
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
	summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
	summary = ' '.join(summary_sentences)
	return summary


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
    #toi_article.title,
    return  toi_article.title,toi_article.summary



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
    
   
@app.route('/')
def index():
	return render_template('index.html')

#RAW TEXT - Start
@app.route('/summ')
def my_form():
	return render_template('summ2.html')

@app.route('/summ',methods=['POST'])
def my_form_post():
	text=request.form['u']
	processed_text=rawtextsummary(text)
	return processed_text

@app.route('/summa',methods=['POST','GET'])
def output():
	x=my_form_post()
	return render_template('summ3.html',x=x)
#RAW TEXT - End

#WEBSITE- Start
@app.route('/summaweb')
def my_form1():
	return render_template('summ4.html')

@app.route('/summaweb',methods=['POST','GET'])
def my_form_post1():
	textweb=request.form['u']
	processed_textweb=websitesummary(textweb)
	return render_template('summ5.html',processed_textweb=processed_textweb)
#WEBSITE - End

#NEWSPAPER - Start
@app.route('/summanews')
def my_form2():
	return render_template('summ6.html')

@app.route('/summanews',methods=['POST','GET'])
def my_form_post2():
	textnews=request.form['u']
	processed_textnewstitle,processed_textnews=newssummary(textnews)
	return render_template('summ7.html',processed_textnewstitle=processed_textnewstitle,processed_textnews=processed_textnews)
#NEWSPAPER - End

#TEXT FILE- Start
@app.route('/summtextfile')
def my_form3():
	return render_template('summ8.html')

@app.route('/summtextfile',methods=['POST'])
def my_form_post3():
	text3=request.form['u']
	processed_textfile=textfilesummary(text3)
	return processed_textfile

@app.route('/summatextfile',methods=['POST','GET'])
def output3():
	x3=my_form_post3()
	return render_template('summ9.html',x3=x3)
#TEXT FILE - End

if __name__ == '__main__':
	app.run(debug=True)

