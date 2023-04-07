import requests
from onion.domain.post import Post

def fetch_data() -> Post:
    # 任意の外部APIからデータを取得する
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. status code: {response.status_code}")
    
    data = response.json()
    
    return Post(
        id=data['id'],
        user_id=data['userId'],
        title=data['title'],
        body=data['body']
    )