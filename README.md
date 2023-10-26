# Classification_Model_Deployment

# Deployment on Google Cloud Platform (GCP)

This guide outlines the steps for deploying a machine learning model using Google Cloud Platform (GCP). Follow these steps to get your deployment up and running.

## Step 1: Clone the Git Repository

```bash
git clone https://github.com/Pulkit0602/Classification_Model_Deployment.git

## Navigate to the project directory:

cd Classification_Model_Deployment

##S tep 2: Build the Docker Image

```bash
docker build -t gcr.io/test-deployment-403209/ml-model-image:latest .

Verify that the image was built successfully:

```bash
docker images
