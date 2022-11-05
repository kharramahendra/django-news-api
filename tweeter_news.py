import requests
import datetime
import tweepy
import facebook


#--------------Facebook Credentials-----------------
graph = facebook.GraphAPI(access_token="EAAHm9MmSr2UBAALq5msmfxoOJf2n33rQi4OZATZB6skga9OMURJiU5dqsfM4ZBM3gI9inN2T3ZACMvFZBZBgaUEG0IqGJkAG3GcK4IutACPe9EezhQ2xoLXD5T2G45E6yQfxCrgPRHRPhZCPxxE3dutjINvcwjokpRnLN0iHmV0I4HY9GfUUWFx",)
#--------------------------------------------------



#-------------NewsApi credentials--------------------
#kharrakaluram@gmail.com
#api_key="d6406f8e4b2c43d2b855218e5ce7ed12"#kharrakaluram
#api_key="3b23c600a77e44068710d0ffaaa08af1"#kharrakalu
api_key="2b07cc7c2f5643e7872b3d6f4abc390a" #kharranews
#----------------------------------------------------



#-----------Twitter credentials------------------------
twitter_auth_keys = {
        "consumer_key"        : "jXdavLhio6Ix09cYhbjccYJbl",
        "consumer_secret"     : "Kt9bRLAsMRLHFqL3s1F9y1EwsfknFDPsdNRbdJphKHHIcUdWHe",
        "access_token"        : "1547867951713308675-awyevDiWcbYCHCkEsDpcCtcxrR0vFX",
        "access_token_secret" : "zSN6bojeYHQ0091GC1ykBsTGIwt6huQU5PxSMnXhS1EJS"
        }
#----------------------------------------------------
auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
#api = tweepy.API(auth)


#-----------------------NEWS-----------------------
def news():
    categories=["general","business","sports","technology","entertainment","health","science"]
    for cat in categories:
    	catnews=requests.get("https://newsapi.org/v2/top-headlines?country=in&category="+cat+"&apiKey="+api_key).json()['articles']
    	for article in catnews:
    		#print(type(article))
    		img=article["urlToImage"]
    		title=str(article['title'])
    		#print(title)
    		desc=str(article['description'])
    		content=str(article['content'])
    		url=str(article['url'])
    		tweet=str(""+title+"   #"+cat+"    article: "+url)
    		#for facebook 1
    		tweet2=str(""+title+"   #"+cat+ "   "+desc+"   article: "+url)
    		if type(img) == str:
    			#for facebook 2
    			graph.put_object(parent_object="me",connection_name="feed",message=tweet2,link=img)
    			#status=api.update_status_with_media(img, tweet)


    		else:
    			#status = api.update_status(status=tweet)
    			pass
news()
#----------------------------------------------------

#---------------------STOCK MARKET-----------------
def stock():
	stock=requests.get("https://newsapi.org/v2/everything?q=nse&apiKey="+api_key).json()['articles']
	i=0
	for article in stock:
		 	if i<11:
		 		img=article['urlToImage']
		 		title=article['title']
		 		desc=article['description']
		 		content=article['content']
		 		url=article['url']
		 		print(url)
		 		tweet=str(title+"   #stockmarket   article: "+url)
		 		if type(img) == str:
		 			status=api.update_status_with_media(img, tweet)
		 		else:
		 			status = api.update_status(status=tweet)
		 		i+=1

#stock()
#----------------------------------------------------


#--------------------CORONA------------------------
def corona():
	corona=requests.get("https://newsapi.org/v2/everything?q=corona&apiKey="+api_key).json()['articles']
	i=0
	for article in corona:
		 	if i<11:
		 		img=article['urlToImage']
		 		title=article['title']
		 		desc=article['description']
		 		content=article['content']
		 		url=article['url']
		 		print(url)
		 		tweet=str(title+"   #corona  article: "+url)
		 		if type(img) == str:
		 			status=api.update_status_with_media(img, tweet)
		 		else:
		 			status = api.update_status(status=tweet)
		 		i+=1

#corona()
#---------------------------------------------------



