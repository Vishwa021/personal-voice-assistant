from serpapi import GoogleSearch


def news(search_news) -> str :

  
  params = {
    "engine": "google_news",
    "q": search_news,
    "gl": "in",
    "hl": "en",
    "api_key": "af3b9ad446a9a6a7bc5d82cc6158df6cb3466555f4917afb034841b94bd312cd"
  }

  search = GoogleSearch(params)
  results = search.get_dict()
  try : 
    news_results1 = f'{results["news_results"][0]["title"]}, {results["news_results"][1]["title"]}, {results["news_results"][2]["title"]}' 
    return news_results1
  except KeyError as e :
    return "Result does not found !"
  


