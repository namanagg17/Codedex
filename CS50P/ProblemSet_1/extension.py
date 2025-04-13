def get_media_type(x):
    # Define a dictionary mapping file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    x = x.strip().lower()

    # Extract the file extension (if any) from the filename
    for extension in media_types:
        if file_name.endswith(extension):
            return media_types[extension]

    # Default media type for unknown or missing extensions
    return "application/octet-stream"


# Prompt the user for a filename
file_name = input("Enter the name of the file: ")

# Get and output the corresponding media type
print(get_media_type(file_name))
