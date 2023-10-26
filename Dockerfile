# Base Image
FROM continuumio/miniconda3

# Copy files from your host system to the container
COPY . /workspace

# Set up the working directory
WORKDIR /workspace

# Create a Conda environment
RUN conda create --name venv python=3.11

# Activate the Conda environment
SHELL ["/bin/bash", "-c"]
RUN echo "source activate venv" >> ~/.bashrc

# Set the environment path for the Conda environment
ENV PATH /opt/conda/envs/venv/bin:$PATH

# Install requirements in the Conda environment
RUN /bin/bash -c "source activate venv && pip install -r requirements.txt"

# Expose a port (assuming your app listens on port 8080)
ENV PORT 8080

# Define the entry point for your application
ENTRYPOINT ["/bin/bash", "-c", "source activate venv && python app.py"]