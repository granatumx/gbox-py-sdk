## Emacs, make this -*- mode: sh; -*-
 
FROM granatumx/gbox-py-base:1.0.0

RUN pip install scanpy==1.5.1

# Install mailjet To implement automated email for bugs #
RUN pip install mailjet_rest

RUN apt-get install -y git

COPY . .
