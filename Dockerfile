FROM python:3.7.2

# Set the working directory to /app
WORKDIR /app

COPY haste /app/haste
COPY setup.py /app/setup.py

RUN pip3 install /app/


CMD ["python","-u","-m","haste.image_analysis_container2"]