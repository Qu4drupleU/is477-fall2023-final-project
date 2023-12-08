import requests
import hashlib
import zipfile
import os

# URL of the dataset
data_url = "https://archive.ics.uci.edu/static/public/186/wine+quality.zip"
# Local path to save the zip file
zip_file_path = 'wine+quality.zip'

# Function to download and verify dataset
def download_and_verify_dataset(url, local_path, expected_hash):
    # Check if the file already exists
    if not os.path.exists(local_path):
        try:
            # Download the file
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Check if the download was successful
            with open(local_path, 'wb') as file:
                file.write(response.content)
        except requests.RequestException as e:
            print(f"Error downloading the file: {e}")
            return False

    # Verify the file's integrity
    with open(local_path, 'rb') as file:
        data = file.read()
        sha256hash = hashlib.sha256(data).hexdigest()
        if sha256hash == expected_hash:
            print("Computed hash matches expected hash for original data.")
            return True
        else:
            print("Computed hash does not match the expected hash for original data.")
            return False

# Function to extract the dataset
def extract_dataset(zip_path, extract_to='data'):
    try:
        os.makedirs(extract_to, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("File unzipped successfully into 'data' directory.")
    except zipfile.BadZipFile:
        print("The downloaded file can not be extracted")

# Expected SHA-256 hash for the dataset
wine_sha256 = '3ed56667f4b828242bd732d7d1dd7f2861e54432239d7fa63877014cbb0304d4'

# Download, verify, and extract the dataset
if download_and_verify_dataset(data_url, zip_file_path, wine_sha256):
    extract_dataset(zip_file_path)
