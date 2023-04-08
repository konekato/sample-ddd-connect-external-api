from sqlalchemy import Column, Integer, String

from ..sqlite import Base
from onion.domain.post import Post


class PostDTO(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

    def to_entity(self) -> Post:
        return Post(
            id=self.id,
            user_id=self.user_id,
            title=self.title,
            body=self.body
        )

    @staticmethod
    def from_entity(post: Post) -> 'PostDTO':
        return PostDTO(
            id=post.id,
            user_id=post.user_id,
            title=post.title,
            body=post.body,
        )