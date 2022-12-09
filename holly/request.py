from urllib.parse import parse_qs


class Request: #Returns parsed environ

    def __init__(self, environ: dict): 
        self.built_get_params_dict(environ['QUERY_STRING'])

    def built_get_params_dict(self, raw_params: str):
        self.GET = parse_qs(raw_params)
        return self.GET

