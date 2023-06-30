import json
from mitmproxy import http

class MockAddon:
    def __init__(self):
        self.mock_responses = {
            'http://example.com': 'mock.json'
        }

    def http(self, flow: http.HTTPFlow) -> None:
        if flow.request.pretty_host == 'example.com':
            with open(self.mock_responses[flow.request.pretty_url]) as f:
                response_data = json.load(f)
            flow.response = http.HTTPResponse.make(
                200,
                json.dumps(response_data),
                {'Content-Type': 'application/json'}
            )
