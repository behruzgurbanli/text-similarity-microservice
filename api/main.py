import shutil
import uuid
import logging
from pathlib import Path
from datetime import datetime
import argparse

from app.config.config import LOG_DIR, UPLOAD_DIR
from app.services.cosine_similarity import find_similars

log_dir = Path(LOG_DIR)
log_dir.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_dir / "app.log", level=logging.INFO, format="%(message)s")

upload_dir = Path(UPLOAD_DIR)
upload_dir.mkdir(parents=True, exist_ok=True)

def log_request(file_uid: str, request_type: str, request_details: str):
    log_entry = f"{datetime.now().isoformat()} - {file_uid} - REQ - {request_type} - {request_details}"
    logging.info(log_entry)

def log_response(file_uid: str, response_details: dict):
    log_entry = f"{datetime.now().isoformat()} - {file_uid} - RESP - {response_details}"
    logging.info(log_entry)

def process_file(file_path: str):
    unique_id = str(uuid.uuid4())
    destination_path = upload_dir / f"{unique_id}_{Path(file_path).name}"
    
    try:
        shutil.copy(file_path, destination_path)
        log_request(unique_id, "csv", Path(file_path).name)

        response = find_similars(destination_path)
        log_response(unique_id, response)

        print(f"File processed successfully. Unique ID: {unique_id}")
        # print(f"Response: {response}")

    except Exception as e:
        error_message = f"Error: {e}"
        logging.error(f"{datetime.now().isoformat()} - {unique_id} - ERROR - {error_message}")
        print(f"An error occurred: {error_message}")

def main():
    parser = argparse.ArgumentParser(description="Process a file for similarity analysis.")
    parser.add_argument("file_path", help="Path to the file to be processed")
    args = parser.parse_args()
    
    process_file(args.file_path)

if __name__ == "__main__":
    main()
