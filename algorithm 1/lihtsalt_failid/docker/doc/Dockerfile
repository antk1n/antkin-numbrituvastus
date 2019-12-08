FROM tensorflow/tensorflow:latest-py3

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /var/www
WORKDIR /var/www

RUN apt-get update

RUN apt-get install -y python3.6
RUN apt-get install -y python3.6-dev

RUN apt-get install -y git

RUN apt-get install gcc
RUN apt-get install -y libglib2.0
RUN apt-get install -y libsm6
RUN apt-get install -y libfontconfig1 libxrender1
RUN apt-get install -y libxtst6

RUN pip3 install Cython
RUN pip3 install cython
RUN pip3 install numpy
RUN pip3 install git+https://github.com/matterport/Mask_RCNN
RUN pip3 install matplotlib
RUN pip3 install setuptools
RUN pip3 install keras==2.2.5 --upgrade
RUN pip3 install imgaug
RUN pip3 install tensorflow==1.14.0
RUN pip3 install opencv_python
RUN pip3 install imutils
RUN pip3 install scikit_image
RUN pip3 install jupyter
RUN pip3 install asyncio
RUN pip3 install GitPython
RUN pip3 install pycocotools
RUN pip3 install tqdm

WORKDIR /var/www/nomeroff-net
