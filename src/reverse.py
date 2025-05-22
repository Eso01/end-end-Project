from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/reverse-word")
async def reverse_word(text: str = Query(...)):
    return {"reversed": text[::-1]}