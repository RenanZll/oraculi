FROM continuumio/miniconda3

MAINTAINER Renan Zelli "renan.zelli@gmail.com"

COPY ./requirements.txt /webapp/requirements.txt

# Add dumb-init
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 /usr/local/bin/dumb-init
RUN chmod a+x /usr/local/bin/dumb-init

WORKDIR /webapp

RUN conda install --yes --file requirements.txt

ENV FLASK_APP=oraculi.py
ENV FLASK_ENV=development

ENTRYPOINT ["/usr/local/bin/dumb-init"]
CMD [ "flask", "run" ]
