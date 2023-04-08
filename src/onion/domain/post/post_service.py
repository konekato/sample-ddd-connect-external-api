from abc import abstractmethod, ABC
from typing import List

from .post import Post


class PostFromJsonplaceholderService(ABC):
    
    @abstractmethod
    def fetch_posts(self) -> List[Post]:
        raise NotImplementedError
