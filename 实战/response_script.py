# https://www.jianshu.com/p/729831067933
import json
from mitmproxy import http

class MockAddon:
    def __init__(self):
        self.mock_responses = {
            'https://api.591.com.tw/api/recom/guessLike': 'mock.json'
        }

    def http(self, flow: http.HTTPFlow) -> None:
        if flow.request.pretty_host == 'api.591.com.tw':
            with open(self.mock_responses[flow.request.pretty_url]) as f:
                response_data = json.load(f)
            flow.response = http.HTTPResponse.make(
                200,
                json.dumps(response_data),
                {'Content-Type': 'application/json'}
            )
