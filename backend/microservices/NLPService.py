import json
# import http.server
import socketserver
from typing import Tuple
from http import HTTPStatus
import requests

from http.server import SimpleHTTPRequestHandler, HTTPServer
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain.vectorstores.redis import Redis
# from langchain.docstore.document import Document

from backend.models import Tweet

### serach hierarchy
# 1. semantic search with filter
# 2. semantic search w/o filter
# 3. API search with filter

def get_embeddings(_hf_api_key, _hf_model_name, _hf_url):
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key = _hf_api_key, model_name = _hf_model_name
    )
    embeddings.api_url = _hf_url
    return embeddings

def get_vectorDB(_redisr_host, _redis_port, _redis_password, embeddings):
    # initialize redis
    rds = Redis(redis_url = f"redis://:{_redis_password}@{_redisr_host}:{_redis_port}/0", index_name = "tweets", embedding = embeddings)
    # load from existing
    rds = Redis.from_existing_index(
        embeddings,
        index_name = "tweets",
        schema = rds.schema,
        key_prefix = 'doc:tweets',
        redis_url = f"redis://:{_redis_password}@{_redisr_host}:{_redis_port}/0"   
    )
    return rds
class NLPService(SimpleHTTPRequestHandler):
    
    embeddings = get_embeddings(
        _hf_api_key = "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",
        _hf_model_name = "bge-base-en-v1.5",
        _hf_url = "https://api-inference.huggingface.co/models/BAAI/bge-base-en-v1.5"
    )
    rds = get_vectorDB(
        _redisr_host = "redis-12311.c11.us-east-1-2.ec2.cloud.redislabs.com",
        _redis_port = 12311,
        _redis_password = 'ff7O5S04jRHY1JXUYLzdbwsRGt1YiYc8',
        embeddings = embeddings
    )

    def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
    

    def parse_json_body(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        return json.loads(body)

    def do_GET(self):
        data = self.parse_json_body()
        content_type = self.headers.get('Content-Type')
        path = self.path.split('/')[-1]
        if path == "sementic_search":
            # sementic search on the query:
            # INPUT: query:str, K:int, 
            # OUTPUT: top K tweets id:List[int]
            headers = {'content-type': 'application/json'}
            topk = data.get('topk', 20)
            query = data.get('query', "")
            results = self.rds.similarity_search_with_score(query, k = topk)
            tweets = []
            for res in results:
                tweet_id = res[0].metadata.get("tweet_id", None)
                # TODO: get tweet from Deck Service
                # payload = {
                #     "id": res.metadata.get("tweet_id", None)
                # }
                # response = requests.request("GET", url = "", data=json.dumps(payload), headers = headers)
                # tweets.append(response.body)
            
            payload = json.dumps({
                "tweets":tweets
            })

            # if content_type == "application/json":
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(payload)

# Set up and start the NLP service
if __name__ == "__main__":
    port = 8010
    server_address = ('', port)
    httpd = HTTPServer(server_address, NLPService)
    print(f"API Gateway running on port {port}...")
    payload = {
        "name": "/nlp/sementic_search",
        "url" : "http://localhost:8010"
    }
    requests.request("POST", url="http://localhost:8003/register", data=json.dumps(payload))
    httpd.serve_forever()

        





    