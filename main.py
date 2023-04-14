from fastapi import FastAPI


# init app
app = FastAPI()


# main root -> Get
@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.post('/')
async def post():
    return {'message': 'Hello From post Method'}


@app.put('/')
async def put():
    return {'message': 'Hello Put method'}


@app.delete('/')
async def delete():
    return {'message': 'Hello Delete Method'}
