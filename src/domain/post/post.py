class Post:
    def __init__(
        self,
        id: int,
        user_id: int,
        title: str,
        body: str
    ):
        self.id: int = id
        self.user_id: int = user_id
        self.title: str = title
        self.body: str = body

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Post):
            return self.id == o.id

        return False