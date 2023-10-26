# Classification_Model_Deployment

# Deployment on Google Cloud Platform (GCP)

This guide outlines the steps for deploying a machine learning model using Google Cloud Platform (GCP). Follow these steps to get your deployment up and running.

1. **Clone the Git Repository**

    ```bash
    git clone https://github.com/Pulkit0602/Classification_Model_Deployment.git
    ```

    Navigate to the project directory:

    ```bash
    cd Classification_Model_Deployment
    ```

2. **Build the Docker Image**

    Build the Docker image, which will be used to deploy your machine learning model. Replace `gcr.io/test-deployment-403209/ml-model-image:latest` with your desired image name and tag:

    ```bash
    docker build -t gcr.io/test-deployment-403209/ml-model-image:latest .
    ```

    Verify that the image was built successfully:

    ```bash
    docker images
    ```

3. **Creating a Kubernetes Cluster**

    Create a Kubernetes cluster on GCP. You can adjust the number of nodes and zone according to your requirements:

    ```bash
    gcloud container clusters create deployment-cluster \
      --num-nodes 1 \
      --zone us-central1-a
    ```

4. **Delete Docker Image (Optional)**

    If you need to delete the Docker image, you can use the `docker rmi` command. Replace `gcr.io/test-deployment-403209/ml-model-image:latest` with the image name and tag you want to delete:

    ```bash
    docker rmi gcr.io/test-deployment-403209/ml-model-image:latest
    ```

5. **Run Docker Image**

    To run the Docker image, use the following command, replacing `gcr.io/test-deployment-403209/ml-model-image:latest` with the image you built:

    ```bash
    docker run gcr.io/test-deployment-403209/ml-model-image:latest
    ```
