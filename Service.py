from fastapi import FastAPI, File, UploadFile
import numpy as np
import tensorflow.keras as keras
from PIL import Image
from io import BytesIO
import numpy as np


app = FastAPI()
model = keras.models.load_model('mnist.keras')


def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))


@app.post("/")
async def read_root(file: UploadFile = File(...)):
    image = load_image_into_numpy_array(await file.read())
    return {'prediction':str(np.argmax(model.predict(np.array([image.reshape(28,28,1)]))))}
