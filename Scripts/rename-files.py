import os

# Folder where files are located
folder_path = 'D:\Downloads\FS25\Test'
new_name = 'Banana #'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Rename files
for i, file_name in enumerate(files):
  # Check if the file is a txt file
  if file_name.lower().endswith('txt'):
    # Construct old and new file paths
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, f'{new_name}{i+1}')

    # Rename the file
    os.rename(old_file_path, new_file_path)
    print(f'Renamed "{file_name}" to "{os.path.basename(new_file_path)}"')

print("Complete")