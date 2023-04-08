from abc import ABC, abstractmethod
from typing import List, Optional

from .post_query_model import PostReadModel
from onion.domain.post import PostRepository, PostFromJsonplaceholderService


class PostCommandUseCase(ABC):

    @abstractmethod
    def create_posts_from_jsonplaceholder_api(self) -> List[PostReadModel]:
        raise NotImplementedError
    

class PostCommandUseCaseImpl(PostCommandUseCase):

    def __init__(self, post_repositry: PostRepository, post_from_jsonplaceholder_service: PostFromJsonplaceholderService):
        self.post_repositry = post_repositry
        self.post_from_jsonplaceholder_service = post_from_jsonplaceholder_service

    def create_posts_from_jsonplaceholder_api(self) -> List[PostReadModel]:
        try:
            posts_from_jsonplaceholder = self.post_from_jsonplaceholder_service.fetch_posts()
            self.post_repositry.insert_posts(posts_from_jsonplaceholder)
        except:
            raise

        return list(map(lambda post: PostReadModel.from_entity(post), posts_from_jsonplaceholder))
