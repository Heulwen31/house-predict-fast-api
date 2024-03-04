from joblib import load
import numpy as np


def house_price_service(features, model_path):
    try:
        print('Loading model...')
        model = load(model_path)
        value = model.predict([features])
        return value
    except Exception as e:
        print(e)
        return np.array([-1])
    finally:
        print("service finish")
