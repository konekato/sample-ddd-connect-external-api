from typing import Optional

from sqlalchemy.orm import Session

from .post_dto import PostDTO
from domain.post import PostRepository, Post


class PostRepositoryImpl(PostRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, post: Post):
        post_dto = PostDTO.from_model(post)
        self.session.add(post_dto)

        try:
            self.session.commit()
        except:
            raise
