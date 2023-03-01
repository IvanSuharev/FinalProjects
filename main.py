from fastapi import FastAPI

from router import user_router, news_router, comment_router

app = FastAPI()


app.include_router(user_router)
app.include_router(news_router)
app.include_router(comment_router)