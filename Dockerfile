FROM continuumio/miniconda3 as oraculi_development

MAINTAINER Renan Zelli "renan.zelli@gmail.com"

WORKDIR /home

COPY ./requirements.txt webapp/requirements.txt

# Add dumb-init
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 /usr/local/bin/dumb-init
RUN chmod a+x /usr/local/bin/dumb-init

WORKDIR ./webapp

RUN conda install --yes --file requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/dumb-init"]
CMD [ "python", "oraculi.py" ]


FROM oraculi_development as oraculi_release

WORKDIR /home/webapp

COPY . .
