from sqlalchemy import Column, Integer, String

from ..database import Base
from domain.post import Post


class PostDTO(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

    def to_model(self) -> Post:
        return Post(
            id=self.id,
            user_id=self.user_id,
            title=self.title,
            body=self.body
        )

    @staticmethod
    def from_model(post: Post) -> 'PostDTO':
        return PostDTO(
            id=post.id,
            name=post.name,
            description=post.description,
        )