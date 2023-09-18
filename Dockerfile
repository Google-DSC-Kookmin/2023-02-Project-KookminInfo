# Use an official Python runtime as a parent image
FROM python:3.9

# Install any needed packages specified in requirements.txt
ADD requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Install Tesseract and any other required system packages
RUN apt-get update && apt-get install -y tesseract-ocr

# Download the Korean language dataset and save it to the correct directory
RUN mkdir -p /usr/share/tesseract-ocr/5/tessdata/
RUN wget https://github.com/tesseract-ocr/tessdata_best/raw/main/kor.traineddata -O /usr/share/tesseract-ocr/5/tessdata/kor.traineddata

# Set the TESSDATA_PREFIX environment variable
ENV TESSDATA_PREFIX /usr/share/tesseract-ocr/5/tessdata/

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "src/app.py"]
