from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Memo(BaseModel):
    id: str
    content: str
    
    
memos = []


app =  FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return '메모 추가 성공'

@app.get("/memos")
def read_Memo():
    return memos

@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo): # request body   m : 기존 내용
    for memo in memos: # memos 배열을 돌면서
        if memo.id == req_memo.id: 
            memo.content = req_memo.content
            return "수정했습니다."
    return "실패"    

@app.delete("/memos/{memo_id}") #memo_id : 전달받은 삭제할 메모의 id
def put_memo(memo_id): 
    for index, memo in enumerate(memos): # for 문을 사용할 때 index와 값을 같이 쓰려면 enumerate() 사용
        if memo.id == memo_id: 
            memos.pop(index)
            return "성공했습니다."
    return "실패"   

app.mount("/",StaticFiles(directory='static', html=True),name='static')