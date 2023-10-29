FROM python:3.11.4 
WORKDIR /frap 
COPY requirements.txt /frap/ 
RUN pip install -r requirements.txt
COPY . /frap 
EXPOSE 5000 
CMD ["python3","run.py"]