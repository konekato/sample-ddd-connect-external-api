from typing import List

from sqlalchemy.orm import Session

from .post_dto import PostDTO
from onion.domain.post import PostRepository, Post


class PostRepositoryImpl(PostRepository):
    
    def __init__(self, session: Session):
        self.session = session

    def insert_posts(self, posts: List[Post]):
        try:
            post_dtos = list(map(lambda post: PostDTO.from_entity(post), posts))
            self.session.bulk_save_objects(post_dtos)
            self.session.commit()
        except:
            self.session.rollback()
            raise
