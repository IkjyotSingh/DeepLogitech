Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests     
 

def times():

     

    # BBC news api

    # following query parameters are used

    # source, sortBy and apiKey

    query_params = {

      "source": "times-news",

      "sortBy": "top",

      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"

    }

    main_url = " https://newsapi.org/v1/articles"
 

    # fetching data in json format

    res = requests.get(main_url, params=query_params)

    open_bbc_page = res.json()
 

    # getting all articles in a string article

    article = open_bbc_page["articles"]
 

    # empty list which will 

    # contain all trending news

    results = []

     

    for ar in article:

        results.append(ar["title"])

         

    for i in range(len(results)):

         

        # printing all trending news

        print(i + 1, results[i])
 

    #to read the news out loud for us

    from win32com.client import Dispatch

    speak = Dispatch("SAPI.Spvoice")

    speak.Speak(results)                 
 
# Driver Code

if _name_ == '_main_':

     

    # function call

    times()