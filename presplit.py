import os

# Get current directory
current_dir = os.getcwd()

# Set directory for images
image_dir = os.path.join(current_dir, "data/obj")

# Get list of image file names
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

# Open text file for writing
with open("data/image_list.txt", "w") as f:
    # Write image file names to file in the format "data/obj/imgX.jpg"
    for i, image_file in enumerate(image_files):
        # Use os.path.join() to properly handle file paths on all systems
        image_path = os.path.join("data/obj", image_file)
        f.write(image_path.replace("\\", "/"))  # Replace backslashes with forward slashes
        if i != len(image_files) - 1:
            f.write("\n")  # Add newline except for last line
