from typing import Iterator, List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from onion.infrastructure.persistence.post import PostRepositoryImpl
from onion.infrastructure.persistence.sqlite import SessionLocal, create_tables
from onion.infrastructure.external_api.jsonplaceholder import PostFromJsonplaceholderServiceImpl
from onion.usecase.post import PostCommandUseCaseImpl, PostCommandUseCase, PostReadModel
from onion.domain.post import PostRepository, PostFromJsonplaceholderService

app = FastAPI()

create_tables()

def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def post_command_usecase(session: Session = Depends(get_session)) -> PostCommandUseCase:
    post_repository: PostRepository = PostRepositoryImpl(session)
    post_from_jsonplaceholder_service: PostFromJsonplaceholderService = PostFromJsonplaceholderServiceImpl()
    return PostCommandUseCaseImpl(post_repository, post_from_jsonplaceholder_service)

@app.post(
    "/save_posts",
    response_model=List[PostReadModel],
    status_code=status.HTTP_201_CREATED,
)
async def save_posts(post_command_usecase: PostCommandUseCase = Depends(post_command_usecase)):
    try:
        posts = post_command_usecase.create_posts_from_jsonplaceholder_api()
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return posts