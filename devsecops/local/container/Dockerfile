# Use the Jupyter notebook base image
# Source: https://hub.docker.com/r/jupyter/base-notebook
FROM jupyter/base-notebook:2021-11-10

# Copy requirements into image
COPY ./src/main/requirements.txt /tmp

# Install likely dependencies
# USER root
# RUN apt-get update
# RUN apt-get install -y \
#     libmariadb3 \
#     libmariadb-dev \
#     gcc
# USER jovyan

# Install requirements
RUN pip3 install -r /tmp/requirements.txt
