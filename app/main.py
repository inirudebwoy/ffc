from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
	# if global flag
	# return disabled

	# if store flag
	# return disabled store
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
