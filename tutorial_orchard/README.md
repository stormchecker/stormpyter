# Notebooks for tutorial

These folder contains the Jupyter notebook for the tutorial as well as model files.

The easiest way to run the notebooks is by building and running the Dockerfile.

```
docker build -t orchard .
docker run -it -p 8080:8080 orchard
```
After running the Dockerfile, visit the localhost link indicated in the commandline output with your web-browser.
This opens the Jupyter lab envirnoment.
The notebooks from the tutorial are available in the `notebooks` directory and follow the same structure as the sections.
The example files, such as the Prism model files, are given in `notebooks/examples`.
