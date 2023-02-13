FROM ubuntu:22.04

WORKDIR /app/src

RUN apt-get update \
	&& apt-get -y install gcc g++ software-properties-common \
	&& add-apt-repository ppa:deadsnakes/ppa \
	&& apt-get update \
	&& apt-get -y install python3.10 python3-pip python3.10-distutils python3-apt python3.10-dev \
 	&& add-apt-repository ppa:ubuntugis/ppa \
 	&& apt-get update \
	&& apt search gdal-bin \
	&& apt-get -y install gdal-bin \
	&& apt-get -y install libpq-dev libgdal-dev

COPY ./src .

RUN pip install --no-cache-dir -r requirements.txt