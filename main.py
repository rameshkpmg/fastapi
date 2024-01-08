from fastapi import FastAPI
app = FastAPI()

@app.get('/home')
def hello():
    return "Hey"


@app.get('/about')
def about():
    return {"message" : "About page"}

@app.get('/home/{id}')
def query(id : int):
    return { "id" : id}

#query parameters
@app.get('/query')
def query_param(param, published):
    return f'{param} value is set and {published}'

@app.get('/params')
def query_parameters(param, a:int = 10, b = False, c:float = 10.34):
    if int(param) > 0:
        return f'{a} and {b} but {c}'
