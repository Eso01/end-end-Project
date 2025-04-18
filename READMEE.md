Password Generator API – CI/CD & Kubernetes Deployment

This project includes a simple Flask-based password generator API, Dockerized and deployed via Kubernetes. It also includes a GitHub Actions CI/CD workflow that lints the code, builds a Docker image, pushes it to Amazon ECR, and can be manually deployed to a Kubernetes cluster.

How to Run the GitHub Actions Workflow

The workflow is located at .github/workflows/ci-cd.yaml and runs automatically on push to the main branch.

Requirements

* A GitHub repository

* AWS ECR repo created

* Secrets configured in GitHub:

   * AWS_ACCESS_KEY_ID

   * AWS_SECRET_ACCESS_KEY

What It Does

* Lints Python code with flake8

* Runs placeholder tests

* Builds and tags Docker image

* Pushes image to ECR

* To trigger the workflow:

To trigger the workflow:
 git push origin main

Manual Kubernetes Deployment Steps

1. Update Deployment with Latest Image

2. Apply Kubernetes Resources:
kubectl apply -f workstation.yaml

3. Verify Deployment:
kubectl get pods -n python-app-ns
kubectl get svc -n python-app-ns

4. test via the external ip assigned on your browser

