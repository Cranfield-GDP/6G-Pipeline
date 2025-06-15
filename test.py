from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
import torch
import torchvision.transforms as transforms
from transformers import AutoModel
import numpy as np
import cv2
import uvicorn

app = FastAPI()

# Load ResNet-50 model from Hugging Face
model_name = "microsoft/resnet-50"
model = AutoModel.from_pretrained(model_name)
model.eval()

# Define preprocessing function
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def process_image(image: Image.Image):
    image = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(image)
    
    # Convert tensor output to an image visualization
    activation = output[0].detach().numpy()
    activation = np.mean(activation, axis=0)
    activation = (activation - activation.min()) / (activation.max() - activation.min()) * 255
    activation = activation.astype(np.uint8)
    activation = cv2.applyColorMap(activation, cv2.COLORMAP_JET)
    return Image.fromarray(cv2.cvtColor(activation, cv2.COLOR_BGR2RGB))

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = Image.open(BytesIO(await file.read())).convert("RGB")
    output_image = process_image(image)
    
    output_io = BytesIO()
    output_image.save(output_io, format="PNG")
    output_io.seek(0)
    return {"filename": file.filename, "message": "Processed successfully", "image": output_io.getvalue()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
 