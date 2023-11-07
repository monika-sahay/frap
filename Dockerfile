FROM python:3.11.4 
WORKDIR /frap 
COPY . /frap 
RUN pip install --upgrade pip && \ 
    pip install --no-cache-dir poetry && \ 
    poetry build && \ 
    pip install dist/frap-0.0.0-py3-none-any.whl && \ 
    pip install -r requirements.txt
EXPOSE 5000 
CMD ["python3", "run.py"]