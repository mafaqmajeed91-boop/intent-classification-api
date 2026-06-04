# FastAPI AI Model API

This project provides a FastAPI application that serves an AI model for predictions. The application is designed to be easily dockerized and deployed to various cloud platforms.

## Files Included
- `app.py`: The main FastAPI application code.
- `model.pkl`: The pre-trained scikit-learn model (Logistic Regression trained on Iris dataset).
- `requirements.txt`: Python dependencies required to run the application.
- `Dockerfile`: Instructions to build a Docker image for the application.
- `README.md`: This file.

## Usage

### 1. Run the API Locally (without Docker)

If you are in a Colab environment or have Python and the dependencies installed, you can run `app.py` directly.

First, install the dependencies:
```bash
pip install -r requirements.txt
```

Then, run the FastAPI application using Uvicorn:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be accessible at `http://0.0.0.0:8000`.

### Endpoints:

- **GET `/`**: Returns a welcome message.
  ```bash
  curl http://localhost:8000/
  ```
  Expected output:
  ```json
  {"message": "AI Model API is running"}
  ```

- **POST `/predict`**: Accepts a list of feature sets and returns predictions and probabilities.
  
  **Request Body Example (JSON):**
  ```json
  [
    { "features": [5.1, 3.5, 1.4, 0.2] },
    { "features": [6.2, 3.4, 5.4, 2.3] }
  ]
  ```
  
  **Example using `curl`:**
  ```bash
  curl -X POST "http://localhost:8000/predict" \
       -H "Content-Type: application/json" \
       -d '[{"features": [5.1, 3.5, 1.4, 0.2]}, {"features": [6.2, 3.4, 5.4, 2.3]}]'
  ```
  Expected output (example):
  ```json
  [
    {"prediction": 0, "probabilities": [0.98, 0.01, 0.01]},
    {"prediction": 2, "probabilities": [0.00, 0.03, 0.97]}
  ]
  ```

## Dockerization

To build and run the application using Docker:

### 1. Build the Docker Image

Navigate to the directory containing `Dockerfile`, `app.py`, `model.pkl`, and `requirements.txt`, then run:
```bash
docker build -t my-fastapi-model-api .
```

### 2. Run the Docker Container
```bash
docker run -p 8000:8000 my-fastapi-model-api
```

The API will be available at `http://localhost:8000`.

## Cloud Deployment Guidance

This Dockerized application can be deployed to various cloud platforms. Here are general steps for some popular choices:

### Render
1.  **Connect GitHub:** Link your GitHub repository (containing `Dockerfile`, `app.py`, `requirements.txt`, `model.pkl`) to Render.
2.  **New Web Service:** Create a new web service in Render, pointing to your repository.
3.  **Configure:** Render will detect the `Dockerfile`. Ensure the port is set to `8000`.
4.  **Deploy:** Render will automatically build the image and deploy the service.

### AWS (ECS/Fargate or EC2)
1.  **Push to ECR:** Push your Docker image to Amazon Elastic Container Registry (ECR).
2.  **ECS/Fargate:**
    *   Create an ECS Cluster.
    *   Define a Task Definition (specify image from ECR, resources, port 8000).
    *   Create an ECS Service to run your task.
    *   Optionally, set up an Application Load Balancer to expose your API.
3.  **EC2:**
    *   Launch an EC2 instance.
    *   Install Docker on the instance.
    *   Pull your Docker image from ECR/Docker Hub.
    *   Run the Docker container using `docker run -p 8000:8000 my-fastapi-model-api`.

### Railway
1.  **Connect GitHub:** Link your GitHub repository to Railway.
2.  **New Project:** Create a new project and connect your repository.
3.  **Configure:** Railway will detect the `Dockerfile` and build/deploy. Configure the exposed port (8000) and startup command if needed.

### Common Deployment Considerations:
-   **Environment Variables:** Configure any sensitive information or dynamic settings as environment variables in your cloud platform's settings.
-   **CI/CD:** Set up Continuous Integration/Continuous Deployment pipelines for automated deployments.
-   **Monitoring & Logging:** Utilize cloud provider tools for monitoring API performance and collecting logs.

from google.colab import files

files.download('app.py')
files.download('model.pkl')
files.download('requirements.txt')
files.download('README.md')
