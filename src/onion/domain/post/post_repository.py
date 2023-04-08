from abc import ABC, abstractmethod
from typing import List

from .post import Post


class PostRepository(ABC):
    
    @abstractmethod
    def insert_posts(self, posts: List[Post]):
        raise NotImplementedError