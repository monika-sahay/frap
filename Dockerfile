FROM python:3.11.4 
WORKDIR /frap 
COPY . /frap/frap 
RUN mv /frap/frap/pyproject.toml /frap/ && \
    mv /frap/frap/setup.cfg /frap/ && \
    mv /frap/frap/.pylintrc /frap/ && \
    mv /frap/frap/run.py /frap/ && \
    pip install --upgrade pip && \ 
    pip install -r frap/requirements.txt && \ 
    python -m build --sdist --wheel ./ && \ 
    pip install dist/frap-0.0.0-py3-none-any.whl

EXPOSE 5000 
CMD ["python3", "run.py"]