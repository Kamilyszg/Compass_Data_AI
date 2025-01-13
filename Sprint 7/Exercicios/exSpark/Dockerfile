FROM jupyter/all-spark-notebook

WORKDIR /home/jovyan/work

EXPOSE 8888

COPY README.md .  
COPY Contador.ipynb .

VOLUME ["/home/jovyan/work"]

CMD ["start-notebook.sh"]