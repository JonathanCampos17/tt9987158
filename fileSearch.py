import os

def search_files(folder_path, search_value):
    # Loops through the files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if search_value in content:
                        print(f"Value found in the file: {filename}")
            except Exception as e:
                print(f"Could not read the file {filename}. Error: {e}")

folder_path = r'C:\'
search_value = "1000557849"

search_files(folder_path, search_value)
