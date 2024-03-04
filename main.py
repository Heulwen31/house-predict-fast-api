from fastapi import FastAPI
import uvicorn
from common.constant import host, port, hanoi_house_price_predict_model_path
from service import house_price_service
import numpy as np
from data.house_info import HouseInfo
app = FastAPI()


@app.post("/hanoi/house/price")
async def hanoi_price(data: HouseInfo):
    print(data)
    features = np.random.rand(1646, )
    house_price = house_price_service.house_price_service(features=features,
                                                          model_path=hanoi_house_price_predict_model_path)

    return {"house_price": house_price.tolist()[0]}


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
