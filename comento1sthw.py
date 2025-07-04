from datasets import load_dataset
from torchvision import transforms
from PIL import Image
import numpy as np
import cv2
import os

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

# 이상치 제거 
def is_too_dark(image, threshold=30):
    gray = image.convert("L")
    mean_brightness = np.mean(np.array(gray))
    return mean_brightness < threshold

def is_too_small(image, pixel_threshold=500):
    gray = image.convert("L")
    binarized = np.array(gray) > 50
    nonzero_pixels = np.count_nonzero(binarized)
    return nonzero_pixels < pixel_threshold

# 저장 폴더
os.makedirs("preprocessed_samples", exist_ok=True)

for i in range(5):
    img = ds[i]["image"]

    # 이상치 필터링
    if is_too_dark(img):
        print(f"{i}: 어두운 이미지, 제외됨")
        continue
    if is_too_small(img):
        print(f"{i}: 너무 작은 객체, 제외됨")
        continue

    processed = preprocess(img)
    augmented = augment(img)

    # 노이즈 제거
    cv_img = np.array(img.resize((224, 224)))
    blurred = cv2.GaussianBlur(cv_img, (5, 5), 0)

    # 저장
    img.save(f"preprocessed_samples/original_{i}.jpg")
    augmented.save(f"preprocessed_samples/augmented_{i}.jpg")
    Image.fromarray(blurred).save(f"preprocessed_samples/blurred_{i}.jpg")










