from abc import ABC, abstractmethod

from .post import Post


class PostRepository(ABC):
    @abstractmethod
    def create(self, post: Post):
        raise NotImplementedError