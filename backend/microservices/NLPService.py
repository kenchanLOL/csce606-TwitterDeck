import json
import http.server
import socketserver
from typing import Tuple
from http import HTTPStatus
import requests

from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores.redis import Redis

class NLPService(http.server.SimpleHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer):
        inference_api_key = "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"
        embeddings = HuggingFaceInferenceAPIEmbeddings(
            api_key=inference_api_key, model_name="bge-base-en-v1.5"
        )
        embeddings.api_url = "https://api-inference.huggingface.co/models/BAAI/bge-base-en-v1.5"
        self.embeddings = embeddings
        self._host = "redis-12311.c11.us-east-1-2.ec2.cloud.redislabs.com"
        self._port = 14255
        self._password = 'TzD9yje5FRM0fvYNx1cAaes7i7pY84ya'
        self.rds = self.init_vectorDB(self)
        
        super().__init__(request, client_address, server)
    

    def parse_json_body(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        return json.loads(body)
    
    # redis_client = redis.StrictRedis(
    # host='127.0.0.1:6379redis-12311.c11.us-east-1-2.ec2.cloud.redislabs.com',
    # port=12311,
    # password='ff7O5S04jRHY1JXUYLzdbwsRGt1YiYc8',
    # ssl=False,
    # decode_responses=False
    # )

    # uri = "mongodb+srv://xutianyi:nqw9TdLszitw28UR@cluster0.al3scwp.mongodb.net/"
    # client = MongoClient(uri)
    # db = client['TwitterDeck_db']
    # collection = db['Tweet']

    def init_vectorDB(self):
        
        # rds = Redis.from_documents(
        #     documents = None,
        #     embedding = self.embeddings,
        #     redius_url = f"redis://:{self._password}@{self._host}:{self._port}/0",
        #     index_name = "tweets"
        # )
        return rds

    def do_GET(self):
        data = self.parse_json_body()
        # if self.path == "/sementic_search":
            # do sementic search on the query:
            # INPUT: query:str, K:int, 
            # OUTPUT: top K tweets id:List[int]
            # headers = {'content-type': 'application/json'}
            # payload = json.dumps({
            #     "queries":data["query"]
            # })
            # response = requests.request("POST", self.embedding_computation_url, data = payload, headers = headers)
            # query_embedding = json.loads(response.text)[0]
            


        # elif self.path == "/add_tweets":
            # add tweets to the vectordb
            # INPUT: tweet: tweet object
            # OUTPUT: status:bool
        

        





    