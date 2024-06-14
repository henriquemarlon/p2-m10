from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import logging

app = FastAPI()

logging.basicConfig(filename='./logs/logs.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

blog_posts: Dict[int, BlogPost] = {}

@app.post("/blog", status_code=201)
async def create_blog_post(post: BlogPost):
    if post.id in blog_posts:
        logger.error('Post with id {} already exists'.format(post.id))
        raise HTTPException(status_code=400, detail="Post already exists")
    blog_posts[post.id] = post
    logger.info('Post created successfully with id {}'.format(post.id))
    return {"status": "success"}

@app.get("/blog", response_model=Dict[int, BlogPost])
async def get_blog_posts():
    if not blog_posts:
        logger.warning('No posts found')
        raise HTTPException(status_code=404, detail="No posts found")
    return blog_posts

@app.get("/blog/{id}", response_model=BlogPost)
async def get_blog_post(id: int):
    post = blog_posts.get(id)
    if not post:
        logger.warning('Post with id {} not found'.format(id))
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.delete("/blog/{id}", status_code=200)
async def delete_blog_post(id: int):
    if id in blog_posts:
        deleted_post = blog_posts.pop(id)
        logger.info('Post deleted successfully with id {}'.format(id))
        return {"status": "success"}
    logger.warning('Post with id {} not found'.format(id))
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/blog/{id}", status_code=200)
async def update_blog_post(id: int, updated_post: BlogPost):
    if id in blog_posts:
        blog_posts[id] = updated_post
        logger.info('Post updated successfully with id {}'.format(id))
        return {"status": "success"}
    logger.warning('Post with id {} not found'.format(id))
    raise HTTPException(status_code=404, detail="Post not found")
