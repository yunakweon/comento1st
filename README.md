# Dataset
- Hugging Face의 food101

# Preprocessing
- Resize: 224*224 크기로 변경
- Grayscale: 흑백 처리
- Normalize: 정규화
- Augmentation
  - RandomHorizontalFlip: 좌우 반전
  - RandomRotation: 회전
  - ColorJitter: 색상 변화 

# Outlier Filtering
- 평균 밝기 기준으로 너무 어두운 이미지 제거
- 객체 크기가 너무 작은 이미지 제거

# Output
- 전처리 결과 5장의 이미지 '/preprocessed_samples/'에 저장
