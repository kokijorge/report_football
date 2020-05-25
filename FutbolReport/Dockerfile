FROM python:3

WORKDIR /src

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD [ "python3", "/src/app.py"]

# docker run --rm -p 8888:8000 --name fut -e SQLALCHEMY_DATABASE_URI='postgresql://postgres:yoursecurepassword@172.17.0.1:5432/testdb' futbolreport 


