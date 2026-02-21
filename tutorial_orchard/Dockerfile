# Build with 
# docker build -t orchard .
# Run with
# docker run -it -p 8080:8080 orchard

FROM stormvogel/stormvogel

# Remove older files
RUN rm -r docs old_notebooks tests README.md

# Install Jupyter extensions
RUN pip install jupyterlab-spellchecker

# Copy files for notebook
RUN mkdir -p notebooks
COPY examples notebooks/examples
COPY *.ipynb notebooks/
COPY *.py notebooks/

# Entrypoint was already defined in stormvogel image
