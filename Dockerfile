FROM ghcr.io/threedify/opensfm:0.5.2 AS main

WORKDIR /source/ThreeDify-SfM

COPY . .

RUN python3 setup.py install

CMD python3 src/main.py

FROM main AS lint

RUN pip3 install -e .[dev]

CMD pylint src && black --check .
