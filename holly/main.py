import re
from typing import List, Type
from holly.exceptions import NotAllowed, NotFound
from holly.urls import Url
from holly.views import View
from holly.request import Request

class Holly:
    
    __slots__ = ('urls')
    
    def __init__(self, urls: List[Url]):
        self.urls = urls
    
    def __call__(self, environ: dict, start_response):
        view: Type[View] = self._get_view(environ)
        request = self._get_request(environ)
        raw_response = self._get_response(environ, view, request)
                                          
        response = raw_response.encode('utf-8') 
        start_response('200 OK', [
            ('Content-Type', 'text/plain; charset=utf-8'),
            ('Content-Length', str(len(response))),
            ])
        return iter([response])

    def _prepare_url(self, url: str): #Deletes slash if it's exist in the end of an address
        if url[-1] == "/":
            url = url[:-1]
        return url

    def _find_view(self, raw_url: str) -> Type[View]: 
        url = self._prepare_url(raw_url)
        for path in self.urls: 
            m = re.match(path.url, url)
            if m is not None:
                return path.view
        raise NotFound

    def _get_view(self, environ: dict) -> Type[View]:
        raw_url = environ["PATH_INFO"] 
        view = self._find_view(raw_url)
        return view

    def _get_request(self, environ: dict):
        return Request(environ)

    def _get_response(self, environ: dict, view: Type[View], request: Request):
        method = environ["REQUEST_METHOD"].lower()
        if not hasattr(view, method):
            return NotAllowed
        return getattr(view, method)(request)
        
