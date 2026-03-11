# Build with 
# docker build -t tutorial .
# Run with
# docker run -it -p 8888:8888 tutorial

FROM quay.io/jupyter/minimal-notebook:ubuntu-24.04

# Install Python libraries from requirements.txt
COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

COPY . .
