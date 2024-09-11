# Text Similarity Microservice

This project is a microservice for text similarity analysis using cosine similarity. It processes CSV files and provides similarity results based on text content. The service logs requests and responses, making it suitable for handling large datasets.

## Features

- Calculates cosine similarity between text contents.
- Logs requests and responses with unique IDs for traceability.
- Handles CSV file uploads and stores them with unique IDs.
- Outputs similarity results in a structured and parseable format.

## Project Structure

- `api/main.py`: Main entry point for the service.
- `app/algorithm/cosine_similarity.py`: Core algorithm for finding similar documents.
- `app/log/`: Directory where logs are stored. Logs include requests and responses with timestamps and file UIDs.
- `app/upload/`: Directory where uploaded CSV files are stored with unique IDs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-similarity-microservice.git
   cd text-similarity-microservice
