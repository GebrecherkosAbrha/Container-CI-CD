# my-app-ci-cd

## Overview

**My App CI/CD** is a Python application that demonstrates a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions and Docker. The project includes automated testing, building Docker images, and pushing them to Docker Hub.

## Features

- Automated testing with `pytest`.
- Docker containerization for easy deployment.
- CI/CD pipeline configured with GitHub Actions.

## Getting Started

### Prerequisites

- Python 3.10 or later
- Docker
- GitHub account with a repository
- Docker Hub account for image storage

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/GebrecherkosAbrha/my-app-ci-cd.git
    cd my-app-ci-cd
    ```

2.  Create a virtual environment and activate it:

```bash
python -m venv venv
```

- **Activate the Virtual Environment:**
  **On Windows:**

  ```bash
      venv\Scripts\activate
  ```

  **On macOS/Linux:**

  ```bash
      source venv/bin/activate
  ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the unit tests:

```bash
pytest
```

2. Build the Docker image locally:

```bash
docker build -t my-app-ci-cd .
```

3. Run the Docker container:

```bash
docker run -d -p 8000:8000 my-app-ci-cd
```

4.  Access the application at `http://localhost:8000`.

## CI/CD Pipeline

The CI/CD pipeline is configured using GitHub Actions. On every push to the `main` branch, the following steps occur:

- **Checkout the repository.**
- **Set up the Python environment.**
- **Install dependencies.**
- **Run tests using pytest.**
- **Build and push the Docker image to Docker Hub.**

## Secrets Management

Make sure to set the following secrets in your GitHub repository:

- **DOCKER_USERNAME:** Your Docker Hub username.
- **DOCKER_PASSWORD:** Your Docker Hub password.
