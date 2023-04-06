from fastapi import FastAPI
from usecase.interactors.save_external_data_interactor import SaveExternalDataInteractor
from usecase.interfaces.input_data import SaveExternalDataInputData
from usecase.interfaces.output_data import SaveExternalDataOutputData

app = FastAPI()

@app.post("/save_external_data")
async def save_external_data():
    # SaveExternalDataInteractorを使ってデータを保存する
    interactor = SaveExternalDataInteractor()
    input_data = SaveExternalDataInputData(...)
    output_data = interactor.execute(input_data)

    # レスポンスを返す
    return output_data