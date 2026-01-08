from fastapi import FastAPI

from storeapi.models.post import UserPost, UserPostIn

app = FastAPI()


post_tabel = {}


@app.post("/", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.dict()
    last_record_id = len(post_tabel)
    new_post = {**data, "id": last_record_id}
    post_tabel[last_record_id] = new_post
    return new_post


@app.get("/", response_model=list[UserPost])
async def get_posts():
    return list(post_tabel.values())
