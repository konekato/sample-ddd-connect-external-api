import requests
from typing import List
from dataclasses import dataclass

from onion.domain.post import Post, PostFromJsonplaceholderService


@dataclass
class PostFromJsonplaceholderDTO:
    id: int
    user_id: int
    title: str
    body: str

    def to_entity(self) -> Post:
        return Post(
            id=self.id,
            user_id=self.user_id,
            title=self.title,
            body=self.body
        )


class PostFromJsonplaceholderServiceImpl(PostFromJsonplaceholderService):

    def __init__(self):
        self.url = 'https://jsonplaceholder.typicode.com'

    def fetch_posts(self) -> List[Post]:
        # 任意の外部APIからデータを取得する
        response = requests.get(f'{self.url}/posts')

        if response.status_code != 200:
            raise Exception(f"Failed to fetch data. status code: {response.status_code}")
        
        data_list = response.json()
        
        post_dtos = list(
            map(
                lambda data: PostFromJsonplaceholderDTO(
                    id=data['id'],
                    user_id=data['userId'],
                    title=data['title'],
                    body=data['body']
                ), data_list
            )
        )
        
        return list(map(lambda post_dto: post_dto.to_entity(), post_dtos))