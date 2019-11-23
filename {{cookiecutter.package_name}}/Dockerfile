FROM python:3
WORKDIR /
RUN pip install pytest
COPY . /
RUN /install.sh

CMD [ "pytest", "tests"]