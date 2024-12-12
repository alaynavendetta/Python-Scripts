#!/usr/bin/python3

# DDHunter.py was created by Alayna N. Ferdarko, https://github.com/alaynavendetta, on 11 December, 2024
# This script parses a .dd file for known headers in order to recover files manually and save them
# to a new folder in the same directory as DDHunter. This is useful for filecarving images from hard drives
# where it may be difficult for programs such as FTKImager or Autopsy/TSK to recover individual files from
# a damaged drive. This program parses through the hex characters in the .dd image to recover files.
# The file headers I have in this program were gained from my time as a student at Bloomsburg University
# from Dr. Scott Inch in Files 1 and 2, and the python programming from Dr. Phil Polstra.

import os

def search_dd_file(dd_file_path, output_dir):
    # File header signatures to search for
    file_signatures = {
        "jpg": b"\xFF\xD8\xFF",
        "gif": b"GIF",
        "mp4": b"\x00\x00\x00\x18ftypmp4",
        "mp3": b"\x49\x44\x33",
        "docx": b"\x50\x4B\x03\x04",
        "xlsx": b"\x50\x4B\x03\x04",
        "txt": b"",  # No fixed header for .txt files
        "pptx": b"\x50\x4B\x03\x04"
    }

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the .dd file in binary mode
    try:
        with open(dd_file_path, "rb") as dd_file:
            data = dd_file.read()

            for file_type, signature in file_signatures.items():
                offset = 0
                file_count = 0

                while True:
                    # Find the next occurrence of the file signature
                    if signature:
                        index = data.find(signature, offset)
                    else:
                        # For .txt files, we extract plain text segments (heuristic-based)
                        index = offset

                    if index == -1:
                        break

                    # Save the file starting at the found index
                    file_count += 1
                    output_file_path = os.path.join(output_dir, f"recovered_{file_type}_{file_count}.{file_type}")

                    with open(output_file_path, "wb") as output_file:
                        if file_type in ["jpg", "gif", "mp4", "mp3"]:
                            # Extract a fixed amount of data (heuristically determined, may need adjustment)
                            output_file.write(data[index:index + 10 * 1024 * 1024])  # 10 MB chunks
                        elif file_type in ["docx", "xlsx", "pptx"]:
                            # Extract ZIP-based formats entirely (assume header to EOF)
                            end_index = data.find(b"\x50\x4B\x05\x06", index)
                            output_file.write(data[index:end_index + 22])  # ZIP file end marker
                        elif file_type == "txt":
                            # Extract plain text segment
                            end_index = data.find(b"\x00", index)  # End at null byte
                            output_file.write(data[index:end_index])

                    print(f"Recovered {file_type} file at offset {index}: {output_file_path}")

                    # Update offset for next search
                    offset = index + len(signature) if signature else end_index

    except FileNotFoundError:
        print(f"File not found: {dd_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
dd_file_path = "path_to_dd_file.dd"  # Replace with the actual path to your .dd file
output_dir = "recovered_files"       # Directory where recovered files will be saved
search_dd_file(dd_file_path, output_dir)
