import os
import shutil
import argparse

def copy_files_recursively(source, destination):
    try:
        # Create the destination directory when it doesn't exist
        if not os.path.exists(destination):
            os.makedirs(destination)
        
        for item in os.listdir(source):
            source_path = os.path.join(source, item)
            if os.path.isdir(source_path):
                # Recursively process subdirectories
                new_destination = os.path.join(destination, os.path.basename(source_path))
                copy_files_recursively(source_path, new_destination)
            else:
                # Process files
                file_ext = os.path.splitext(item)[1][1:].lower()  # Make the file extension without the dot
                ext_dir = os.path.join(destination, file_ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                shutil.copy2(source_path, ext_dir)
    except Exception as e:
        print(f"Error processing {source}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them into subdirectories based on file extensions.")
    parser.add_argument("source", help="Path to the source directory")
    parser.add_argument("destination", nargs='?', default="dist", help="Path to the destination directory (default is 'dist')")
    args = parser.parse_args()
    
    source = args.source
    destination = args.destination
    
    if not os.path.exists(source):
        print(f"Error: Source directory '{source}' does not exist.")
        return
    
    copy_files_recursively(source, destination)
    print("All files copied and sorted successfully.")

if __name__ == "__main__":
    main()