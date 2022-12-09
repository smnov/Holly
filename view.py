from holly.views import View
from holly.request import Request

class Homepage(View):
    
    def get(self, request: Request, *args, **kwargs):
        return "Hello world from view"


class EpicMath(View):

    def get(self, request: Request, *args, **kwargs):
        first_arg = request.GET.get('first')
        if not first_arg or not first_arg[0].isnumeric():
            return f'first пустое либо не является числом'
        second_arg = request.GET.get('second')
        if not second_arg or not second_arg[0].isnumeric():
            return f'second пустое либо не является числом'
