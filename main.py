import uvicorn
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests
from datetime import datetime, timedelta
app = FastAPI()

# News API 키 설정
API_KEY = ""
@app.get("/everything/")
async def get_everything(
        from_date: str = Query(..., description="검색 시작 날짜 (YYYY-MM-DD 형식)"),
        q: str = Query("", description="검색 키워드")
):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": API_KEY,
        "sortBy": "publishedAt",
        "from": from_date
    }

    try:
        from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
        params["from"] = from_date_obj.strftime("%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Please use YYYY-MM-DD.")

    if q:
        params["q"] = q
    else:
        # 기본 검색 키워드 설정
        params["q"] = "news"

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["articles"]
    else:
        raise HTTPException(status_code=response.status_code, detail="API 요청 실패")
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)