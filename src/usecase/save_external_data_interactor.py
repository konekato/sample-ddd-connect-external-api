from domain.repositories.repository_interface import RepositoryInterface
from usecase.interfaces.input_data import SaveExternalDataInputData
from usecase.interfaces.output_data import SaveExternalDataOutputData
from infrastructure.external_api.api_client import APIClient

class SaveExternalDataInteractor:
    def __init__(self, repository: RepositoryInterface, api_client: APIClient):
        self.repository = repository
        self.api_client = api_client

    def save_external_data(self, input_data: SaveExternalDataInputData) -> SaveExternalDataOutputData:
        # 外部APIからデータを取得
        external_data = self.api_client.get_data(input_data.target_url)

        # 取得したデータをデータベースに保存
        self.repository.save_data(external_data)

        # 保存したデータを返す
        return SaveExternalDataOutputData(data=external_data)