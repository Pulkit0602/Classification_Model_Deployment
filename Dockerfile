#Base Image
FROM continuumio/miniconda3

#Copy file from system to the containeer
COPY . /workspace

#Set up working Directory
WORKDIR /workspace

#Setup conda environmet
RUN conda create --name venv python=3.11
RUN echo "source activate venv" ~/.bashrc

ENV PATH /opt/conda/envs/venv/bin:$PATH

#Install all the Requirments
RUN /opt/conda/envs/venv/bin/pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["/opt/conda/envs/venv/bin/python", "app.py"]