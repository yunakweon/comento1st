import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, PolynomialRegression, LogisticRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error, precision_score, recall_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer

# 데이터셋 로드
ratings = pd.read_csv('ratings.csv')  # 영화 평점 데이터
movies = pd.read_csv('movies.csv')  # 영화 정보 데이터

# 데이터 전처리
X = ratings[['userId', 'movieId']]
y = ratings['rating']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 딕셔너리
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Lasso Regression': Lasso(alpha=1.0),
    'ElasticNet Regression': ElasticNet(alpha=1.0, l1_ratio=0.5),
    'Polynomial Regression': make_pipeline(PolynomialFeatures(degree=2), LinearRegression()),
    'Logistic Regression': LogisticRegression(max_iter=1000)
}

# 결과 저장
results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # RMSE 계산
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    if name == 'Logistic Regression':
        # 이진화: 3.5 이상을 1로, 나머지는 0으로 설정
        threshold = 3.5
        y_pred_classes = (y_pred >= threshold).astype(int)
        y_test_classes = (y_test >= threshold).astype(int)

        # Precision, Recall 계산
        precision = precision_score(y_test_classes, y_pred_classes)
        recall = recall_score(y_test_classes, y_pred_classes)
        results[name] = {'RMSE': rmse, 'Precision': precision, 'Recall': recall}
    else:
        results[name] = {'RMSE': rmse}

# 결과 출력
for name, metrics in results.items():
    print(f"{name}: {metrics}")

