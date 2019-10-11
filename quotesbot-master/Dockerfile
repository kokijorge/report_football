FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "scrapy", "crawl", "as-xpath", "-o", "as.json" ]
CMD [ "python3", "try_afinn.py"]