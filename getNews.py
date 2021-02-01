from newsapi.newsapi_client import NewsApiClient
from pandas.io.json import json_normalize
import pandas as pd
from ActualNewsClassification import Preprocessing, ClassifyHeadlines

def top_headlines(country, topic):  
   newsapi = NewsApiClient(api_key="3d4657a3a0ff42db9243b2e01d8357b8")          
   top_headlines =newsapi.get_top_headlines(category=topic,
   language='en',country=country)     
   top_headlines=json_normalize(top_headlines['articles'])   
   newdf = top_headlines[["title","url"]]
   newdfBackup = newdf
   newdf = Preprocessing(newdf)

   PositiveHeadlines, NegativeHeadlines = ClassifyHeadlines(newdf, 120000, 28309, 29183)

   print(PositiveHeadlines, "\n--------------------------------\n", NegativeHeadlines)

   PositiveUrl = {}
   for i in PositiveHeadlines:
      PositiveUrl[newdfBackup.iloc[i]['title']] = newdfBackup.iloc[i]['url']

   print(PositiveUrl)

   return PositiveUrl

