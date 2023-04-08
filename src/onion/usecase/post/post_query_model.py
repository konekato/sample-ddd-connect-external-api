from pydantic import BaseModel, Field

from onion.domain.post import Post


class PostReadModel(BaseModel):
    id: int = Field(example=999)
    user_id: int = Field(example=999)
    title: str = Field(example="Sample title.")
    body: str = Field(example="This is sample text.")
    
    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(post: Post) -> "PostReadModel":
        return PostReadModel(
            id=post.id,
            user_id=post.user_id,
            title=post.title,
            body=post.body,
        )