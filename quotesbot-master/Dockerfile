FROM python:3

# https://hub.docker.com/r/joyzoursky/python-chromedriver/dockerfile

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99


WORKDIR /usr/src/app


COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "scrapy", "crawl", "as-xpath", "-o", "as.json" ]
#CMD [ "python3", "try_afinn.py"]
CMD [ "scrapy", "crawl", "jugadores-xpath", "-o", "jugadores.json" ]

