import os
import zipfile

def extract_zip(zip_path, extract_to):
    """Extracts the zip file to a specified directory."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted: {zip_path} to {extract_to}")
    except Exception as e:
        print(f"Error extracting {zip_path}: {e}")

def search_in_import_folder(folder_path, search_value):
    """Searches for the value only inside the 'in/import' folder."""
    for root, _, files in os.walk(folder_path):
        if os.path.basename(root) == "import" and os.path.basename(os.path.dirname(root)) == "in":
            print(f"Searching in: {root}")
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        if search_value in content:
                            print(f"Value found in: {file_path}")
                except Exception as e:
                    print(f"Could not read {filename}. Error: {e}")

def process_folder(folder_path, search_value):
    """Processes the folder, extracts zip files, and searches 'in/import' folders."""
    temp_extract_path = os.path.join(folder_path, 'temp_extracted')
    os.makedirs(temp_extract_path, exist_ok=True)

    # Extract all zip files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if zipfile.is_zipfile(file_path):
            extract_zip(file_path, temp_extract_path)

    # Search for the 'in/import' folder and search within it
    for root, dirs, _ in os.walk(temp_extract_path):
        if "in" in dirs:  # Check if the 'in' directory exists
            in_path = os.path.join(root, "in")
            search_in_import_folder(in_path, search_value)

# Specify folder path and search value
folder_path = r'C:\Users\jonat\OneDrive\Desktop\tester'
search_value = "1000557849"

process_folder(folder_path, search_value)
