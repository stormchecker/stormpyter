# Build with 
# docker build -t orchard .
# Run with
# docker run -it -p 8080:8080 orchard
FROM movesrwth/stormpy:1.12.0



# Set-up virtual environment
############################
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install stormvogel
RUN pip install stormvogel

# Install PAYNT
RUN git clone https://github.com/randriu/synthesis.git \
	&& cd synthesis \
	&& pip install -r build-requirements.txt \
	&& pip install . --no-build-isolation

# Install LP solver
RUN pip install pyscipopt

# Install Jupyter lab
RUN pip install jupyterlab
RUN pip install jupyterlab-spellchecker

# Copy the project files into the container
COPY . /app
WORKDIR /app


# create /root/.jupyter directory
RUN mkdir -p /root/.jupyter

# Create a random password for the Jupyter Lab
RUN PASSWORD=$(echo -n $(date +%s) | sha1sum | awk '{print $1}') && echo $PASSWORD > /root/jupyter_password.txt

# Set identity provider class to token based
# Set the token to the password
RUN echo "c.NotebookApp.token = '$(cat /root/jupyter_password.txt)'" >> /root/.jupyter/jupyter_notebook_config.py

RUN echo "echo -e '\033[44;37mWelcome to the stormvogel container!\033[0m'" >> /root/.bashrc
RUN echo "\033[34m         =======                               \n\
      =============                            \n\
     ===============                           \n\
    =================           =====          \n\
    ======%%%=========        ============     \n\
   =====================     ===============   \n\
  ==========================================   \n\
     ====================================      \n\
    ================================         \n\
    =============================            \n\
    ==========++===============              \n\
     ==========##===============#            \n\
      ==========###===========#              \n\
        ==========####=====##                \n\
        ===========######                  \n\
             ==   ==                       \n\
            ===   ==                       \n\
         ====   ====                       \n\
            ====                         \033[0m" > /root/bird.txt
RUN echo "cat /root/bird.txt" >> /root/.bashrc
RUN echo "echo -e '\033[44;37mRun this container with -p 8080:8080 to get access to the Jupyter Lab from your host computer.\033[0m'" >> /root/.bashrc
# Print the Jupyter Lab URL, including the password
RUN echo "echo -e '\033[44;37mJupyter Lab will be running at http://localhost:8080/?token=$(cat /root/jupyter_password.txt) in a minute or so.\033[0m'" >> /root/.bashrc
# Print how to restart this docker instance after leaving it
RUN echo "echo -e \"\033[44;37mTo restart this container, run docker start -i \$(hostname)\033[0m\"" >> /root/.bashrc

# Start a bash shell, but run Jupyter Lab inside Poetry in the background on port 8080
CMD ["bash", "-c", "setsid jupyter lab --ip 0.0.0.0 --port=8080 --no-browser --allow-root 0</dev/null > /app/jupyter_lab.log 2>&1 & exec bash"]
