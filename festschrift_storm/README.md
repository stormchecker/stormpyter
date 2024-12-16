# Jupyter notebooks for "Riding the Storm in a Probabilistic Model Checking Landscape"
This set of notebooks is based on the paper with the same name,
which appeared in a Festschrift dedicated to Joost-Pieter Katoen's 60th birthday. 
The notebook is meant as a living document,
that helps to run some of the advanced features of Storm. 
The current version of the notebook is, however, rather basic. 
Feel free to submit PRs!


## Getting started
You can start the Jupyterlab locally using [Docker](https://www.docker.com/).
First, build the Docker container with
```
docker build -t movesrwth/stormpyter-festschrift .
```
Then start the Docker container with the following command:
```
docker run -it --rm -p 8888:8888 movesrwth/stormpyter-festschrift jupyter notebook --NotebookApp.default_url=/lab/ --ip=0.0.0.0 --port=8888
```
You can find the URL to the notebook in the output.
