from api import API

app = API()

@app.route("/home")
def home(request, response):
    response.text = "Главная"
    return request

@app.route("/about")
def about(request, response):
    response.text = "About"
    return request

@app.route("/hello/{name}")
def hello(request, response, name):
    response.text = f"Hello, {name}"
