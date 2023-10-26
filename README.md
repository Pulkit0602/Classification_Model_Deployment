# Classification_Model_Deployment

***Note Change test-deployment-40320 --> To your Project Id mentioned in GCP***

# Deployment on Google Cloud Platform (GCP)

This guide outlines the steps for deploying a machine learning model using Google Cloud Platform (GCP). Follow these steps to get your deployment up and running.

1. **Clone the Git Repository**
    ```bash
    git clone https://github.com/Pulkit0602/Classification_Model_Deployment.git
    cd Classification_Model_Deployment
    ```

2. **Build the Docker Image and Push to GCP Registry**
    Build the Docker image and push it to the Google Cloud Platform (GCP) registry. Replace `gcr.io/test-deployment-403209/ml-model-image:latest` with your desired image name and tag. Ensure you use your GCP project ID.
    ```bash
    gcloud builds submit --tag gcr.io/test-deployment-403209d/ml-model-image:latest
    ```

3. **Check the Docker Image Build**
    List the Docker images in your GCP repository to verify that the image was built successfully. Make sure to replace `gcr.io/test-deployment-403209` with your GCP project ID.
    ```bash
    gcloud container images list --repository=gcr.io/test-deployment-403209d
    ```

4. **Creating a Kubernetes Cluster**
    Create a Kubernetes cluster on GCP. You can adjust the number of nodes and the zone according to your requirements.
    ```bash
    gcloud container clusters create deployment-cluster --num-nodes 1 --zone us-central1-a
    ```

5. **To Delete Docker Image (Optional)**
    If you need to delete the Docker image, you can use the `gcloud container images delete` command. Replace `gcr.io/test-deployment-403209d/ml-model-image:latest` with the image name and tag you want to delete.
    ```bash
    gcloud container images delete gcr.io/test-deployment-403209d/ml-model-image:latest
    ```

6. **Run Docker Image**
    To deploy your containerized application using Google Cloud Run, use the following command. Replace `gcr.io/test-deployment-403209/ml-model-image` with the image you built, and specify the service name and any additional settings as needed.
    ```bash
    gcloud run deploy --image gcr.io/test-deployment-403209d/ml-model-image
    ```

7. **Start with Kubernetes Deployment (If Docker container is running perfectly)**
    - First, change the image in your Deployment.yaml file.
    ```bash
    vim Deployment.yaml
    ```

    - Run the Deployment Definition.
    ```bash
    kubectl create -f deployment.yaml
    ```

    - Check the number of Pods; it should be equal to the replica mentioned. If there are no errors, proceed with services.
    ```bash
    kubectl get pods
    ```

8. **Run the Services Definition**
    ```bash
    kubectl create -f service.yaml
    ```

9. **Obtain IP Access**
    Run the following command to get the service's IP address.
    ```bash
    kubectl get service -o wide
    ```

***Enjoy The Deployment***
