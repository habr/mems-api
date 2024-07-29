# Memes API

This project provides an API for managing a collection of memes. The project consists of two services: a public API service with business logic and a private API service for handling media files using S3-compatible storage (MinIO).

## Features

- **GET /memes**: Retrieve a list of all memes (with pagination).
- **GET /memes/{id}**: Retrieve a specific meme by its ID.
- **POST /memes**: Add a new meme (with image and text).
- **PUT /memes/{id}**: Update an existing meme.
- **DELETE /memes/{id}**: Delete a meme.

## Requirements

- Docker
- Docker Compose

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/habr/memes-api.git
   cd memes-api
2. Start the services using Docker Compose:
   ```bash
   docker-compose up --build
3. Access the API documentation:
   1. Public API: http://localhost:8000/docs
   2. Media API: http://localhost:8001/docs
4. Running Tests
   ```bash
   docker-compose run memes_api pytest
   docker-compose run media_api pytest