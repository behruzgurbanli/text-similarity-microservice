# Text Similarity Microservice

This project is a microservice designed for text similarity analysis using cosine similarity. It allows users to upload CSV files, processes text content, and outputs similarity results, making it ideal for handling large datasets. The service logs requests and responses, providing traceability and accountability in text similarity computations.

## Features

- **Cosine Similarity Calculation**: Computes cosine similarity between text contents from uploaded CSV files.
- **Logging**: Detailed logging of requests and responses, including timestamps, unique IDs, and input/output details.
- **File Handling**: Efficiently manages CSV file uploads and stores them with unique identifiers.
- **Scalable Design**: Built with FastAPI, making it lightweight and easy to extend for more complex similarity measures.

## Project Structure

- **`api/main.py`**: The main entry point of the service, handling API requests and routing.
- **`app/algorithm/cosine_similarity.py`**: Implements the core algorithm to compute cosine similarity between texts.
- **`app/config.py`**: Configuration file managing the settings used across the application.
- **`app/log/`**: Directory where logs are stored. Logs are organized with date and time stamps and include details of requests and responses.
- **`app/upload/`**: Directory for storing uploaded CSV files. Each file is stored with a unique identifier to avoid conflicts.

## Prerequisites

- Python 3.8 or higher installed on your system.
- Git installed for cloning the repository.

## Installation

### Step 1: Clone the Repository

Clone the GitHub repository to your local machine using the command:

```bash
git clone https://github.com/your-username/text-similarity-microservice.git
cd text-similarity-microservice
```

### Step 2: Set Up a Virtual Environment

It is recommended to create a virtual environment to isolate the dependencies for this project. You can create one using the following commands:

# On macOS and Linux
```bash
python3 -m venv venv
```

# On Windows
```bash
python -m venv venv
```

Activate the virtual environment:
# On macOS and Linux
```bash
source venv/bin/activate
```

# On Windows
```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Configuration
### Configuring Settings
The configuration settings are managed in config.py. You can modify the following settings as per your needs:

Logging Settings: Adjust log file locations, log levels, and formats.
File Storage Paths: Customize paths where uploaded files and logs are stored.
Similarity Thresholds: Set thresholds for considering texts as similar.

## Running the Program
### Step 1: Start the Server
To start the FastAPI server, run the following command:

Run the server with Uvicorn
```bash
uvicorn main:app --reload
```
- The --reload flag enables hot-reloading, which automatically restarts the server when code changes are detected.
- By default, the server runs on http://127.0.0.1:8000. You can access the interactive API documentation at http://127.0.0.1:8000/docs.

### Step 2: Upload a CSV File
Use the /upload endpoint to upload a CSV file containing text data. The CSV should have a structure where one column contains the text content to be analyzed.

You can upload files directly via the Swagger UI at http://127.0.0.1:8000/docs or using a tool like curl:
```bash
curl -X POST "http://127.0.0.1:8000/upload" -F "file=@your-file.csv"
```

### Step 3: View Similarity Results
Once the file is uploaded, the service will process the text and calculate similarities. You can view the results by accessing the /results endpoint.

### Step 4: Checking Logs
Logs are stored in the app/log/ directory. The logs are separated into request and response logs for better traceability. Each log entry includes:

- Date & Time: Precise timestamp down to milliseconds.
- File UID: Unique identifier for the uploaded file.
- Request Details: File type, request parameters, etc.
- Response Details: Similarity results in a structured format.

## Testing
Testing can be done by uploading different CSV files and comparing the output results. Ensure that the CSV files have clean data for accurate similarity measurement.

