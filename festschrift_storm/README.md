# Jupyter notebooks for "Riding the Storm in a Probabilistic Model Checking Landscape"

## Getting started
You can also start the Jupyterlab locally using [Docker](https://www.docker.com/).
First, build the Docker container with
```
docker build -t movesrwth/stormpyter-festschrift .
```
Then start the Docker container with the following command:
```
docker run -it --rm -p 8888:8888 movesrwth/stormpyter-festschrift jupyter notebook --NotebookApp.default_url=/lab/ --ip=0.0.0.0 --port=8888
```
You can find the URL to the notebook in the output.
