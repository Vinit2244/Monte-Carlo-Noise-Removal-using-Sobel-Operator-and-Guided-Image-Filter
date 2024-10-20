import os

def print_directory_structure(root_dir, prefix="", exclude_dirs=None, exclude_files=None):
    # Set default for exclude_dirs and exclude_files if not provided
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_files is None:
        exclude_files = []
    
    # Get the contents of the directory
    contents = os.listdir(root_dir)
    # Sort contents to make it consistent (folders first, then files)
    contents.sort(key=lambda x: (os.path.isfile(os.path.join(root_dir, x)), x))
    
    # Loop through the contents
    for i, item in enumerate(contents):
        path = os.path.join(root_dir, item)
        
        # Skip directories that are in the exclude list
        if os.path.isdir(path) and item in exclude_dirs:
            continue
        
        # Skip files that are in the exclude list
        if os.path.isfile(path) and item in exclude_files:
            continue
        
        # Check if it's the last item in the current level to print └── instead of ├──
        if i == len(contents) - 1:
            connector = "└──"
        else:
            connector = "├──"
        
        # Print the directory or file with the proper prefix
        if os.path.isdir(path):
            print(f"{prefix}{connector} 📁 {item}/")
            # Recurse into the directory, adding "│   " if not the last item, otherwise just "    "
            new_prefix = prefix + ("    " if connector == "└──" else "│   ")
            print_directory_structure(path, new_prefix, exclude_dirs, exclude_files)
        else:
            print(f"{prefix}{connector} 📄 {item}")

# Example usage
exclude_folders = ['env', '.git']   # Folders to exclude
exclude_files = ['.DS_Store']       # Files to exclude

# Get the project name from the current directory
project_name = os.path.basename(os.getcwd())
    
# Print the project name at the top
print(f"📦 {project_name}")

print_directory_structure(".", exclude_dirs=exclude_folders, exclude_files=exclude_files)