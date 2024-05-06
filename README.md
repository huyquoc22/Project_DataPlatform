# Hệ thống phát hiện gian lận thẻ tín dụng thời gian thực

Built with FastAPI, Streamlit and Docker.
### Dataset
Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Modelling
- Logistic Regression
- Random Forest

## Running:

1. create AIservice
```
docker network create AIservice
```
2. Run command
```docker
docker-compose up -d --build
```
3. Result

- FastAPI http://localhost:8000 

- Streamlit UI http://localhost:8501.

4. View Logs
```
docker-compose logs
```