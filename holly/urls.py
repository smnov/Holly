from dataclasses import dataclass
from holly.views import View
from typing import Type

@dataclass
class Url:
    url: str
    view: Type[View]
