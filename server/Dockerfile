from python:3.10-bullseye

RUN pip install fastapi
RUN pip install uvicorn

# Set the working directory in the container
WORKDIR /app

COPY py/ .

# Set the default port if not provided
ENV PORT=8000

RUN echo $PORT

# Expose the port dynamically
EXPOSE ${PORT}

# Command to run the FastAPI app
CMD ["python", "server.py"]