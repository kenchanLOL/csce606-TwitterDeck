import requests
Bearer = "AAAAAAAAAAAAAAAAAAAAAJQ0qAEAAAAAHZeVavLaRkoSSgUKPR45YnVGJHc%3DuoKDntDqkfHnSkteqrObrsZbDKmeouijrOGURPE7pRjgGHbASj"
url = "https://api.twitter.com/1.1/search/tweets.json"
query = {}
if __name__ == "__main__":
    response = requests.get(url, params = query)