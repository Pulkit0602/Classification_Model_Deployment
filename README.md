# Classification_Model_Deployment

***Note Change test-deployment-40320 --> To your Project Id mentioned in GCP***

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

2. **Build the Docker Image and Push to GCP Registry**

    Build the Docker image and push it to the Google Cloud Platform (GCP) registry. Replace `gcr.io/test-deployment-403209/ml-model-image:latest` with your desired image name and tag. Ensure you use your GCP project ID.

    ```bash
    gcloud builds submit --tag gcr.io/your-project-id/ml-model-image:latest
    ```

3. **Check the Docker Image Build**

    List the Docker images in your GCP repository to verify that the image was built successfully. Make sure to replace `gcr.io/test-deployment-403209` with your GCP project ID.

    ```bash
    gcloud container images list --repository=gcr.io/your-project-id
    ```

4. **Creating a Kubernetes Cluster**

    Create a Kubernetes cluster on GCP. You can adjust the number of nodes and the zone according to your requirements:

    ```bash
    gcloud container clusters create deployment-cluster \
      --num-nodes 1 \
      --zone us-central1-a
    ```

5. **Run Docker Image**

    To deploy your containerized application using Google Cloud Run, use the following command. Replace `gcr.io/test-deployment-403209/ml-model-image` with the image you built, and make sure to specify the service name and any additional settings as needed.

    ```bash
    gcloud run deploy --image gcr.io/your-project-id/ml-model-image
    ```

6. **If the Docker container is running perfectly, start with Kubernetes Deployment**

    - **Change the image in Deployment.yaml**

      Use a text editor like `vim` to edit the `Deployment.yaml` file and change the image to the one you've pushed to the GCP container registry.

      ```bash
      vim Deployment.yaml
      ```

    - **Run the Deployment Definition**

      Create the Kubernetes Deployment using the updated `Deployment.yaml` file.

      ```bash
      kubectl create -f Deployment.yaml
      ```

    - **Check the Number of Pods**

      Verify that the number of pods created matches the desired replicas specified in your `Deployment.yaml` file. This ensures your deployment is working as expected.

      ```bash
      kubectl get pods
      ```

    - **Run the Services Definition**

      Create the Kubernetes Service using the `service.yaml` file.

      ```bash
      kubectl create -f service.yaml
      ```

    - **Get IP Access**

      Obtain the IP address for accessing your service.

      ```bash
      kubectl get service -o wide
      ```

