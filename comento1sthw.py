from datasets import load_dataset
from torchvision import transforms
from PIL import Image
import numpy as np
import cv2

# 데이터셋 불러오기
ds = load_dataset("ethz/food101", split="train[:5]")

# 전처리
preprocess = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.Grayscale(),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

# 데이터 증강
augment = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(20),
    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3)
])

for i in range(5):
    img = ds[i]["image"]
    processed = preprocess(img)
    augmented = augment(img)

    # 노이즈 제거
    cv_img = np.array(img.resize((224, 224)))
    blurred = cv2.GaussianBlur(cv_img, (5, 5), 0)

    # 저장
    img.save(f"original_{i}.jpg")
    augmented.save(f"augmented_{i}.jpg")
    Image.fromarray(blurred).save(f"blurred_{i}.jpg")










