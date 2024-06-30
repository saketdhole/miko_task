import os

import requests

from tools.common import Common
from tools.readconfig import ReadConfig

CONFIG_PATH = os.path.join(os.getcwd(), "environment", "Config.ini")

class ComponentBase:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers['Content-Type'] = 'application/json;charset=utf-8'
        self.logger = Common().get_logs()
        conf = ReadConfig(CONFIG_PATH)
        self.baseurl = conf.api_url()

    def get_headers(self):
        return self.session.headers

    def update_session_headers(self, header: dict):
        self.session.headers.update(header)

    def remove_session_header(self, header_name):
        self.session.headers.pop(header_name)

    def assert_request(self, method, url, payload=None, params=None, headers=None, codecheck=200, **kwargs):
        response = self.session.request(method, url, headers=headers, json=payload, params=params, **kwargs)
        all_headers = self.session.headers
        if headers:
            all_headers.update(dict(headers))

        self.logger.info(f'URL: {url} / {method}')
        self.logger.info(f'REQUEST PAYLOAD: {payload or kwargs.get("data", {})}')
        self.logger.info(f'REQUEST PARAMS: {params}')
        self.logger.info(f'REQUEST HEADERS: {all_headers}')
        self.logger.info(f'RESPONSE STATUS CODE: {response.status_code}')
        self.logger.info(f'RESPONSE HEADERS: {response.headers}')
        self.logger.info(f"RESPONSE: {response.json()}")

        assert response.status_code == int(codecheck), "Unexpected Response code"

        return response

    def verify_json_content(self, json_object, attributes):

        for attr in attributes:
            if not (attr in json_object):
                assert False, f"Response does not contain {attr} attribute"
