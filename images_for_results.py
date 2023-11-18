import os
import shutil


def copy_files(src_folder, dst_folder, subdirs, start_time, end_time):
    for root, dirs, files in os.walk(src_folder):
        print(f"Processing directory: {root}")

        # Check if all subdirs are present
        if any(subdir in dirs for subdir in subdirs):
            last_dir = os.path.basename(root)
            print(f"Last directory: {last_dir}")

            # Check if the last directory is within the time range
            if last_dir.isdigit() and int(last_dir) in range(start_time, end_time + 1):
                src_path = os.path.join(root, last_dir)
                dst_path = os.path.join(dst_folder, last_dir)
                print(f"Copying files from {src_path} to {dst_path}")

                # Create the destination directory if it doesn't exist
                os.makedirs(dst_path, exist_ok=True)

                # Iterate over files in the source directory and copy them to the destination
                for filename in files:
                    src_file = os.path.join(src_path, filename)
                    dst_file = os.path.join(dst_path, filename)
                    shutil.copy2(src_file, dst_file)

                print(f"Files from {src_path} copied to {dst_path}")
            else:
                print(f"Last directory {last_dir} is not within the time range")
        else:
            print(f"Not all subdirectories {subdirs} are present in {dirs}")


if __name__ == "__main__":
    # Example usage:
    src_folder = 'data/img'
    dst_folder = 'inference/images'
    subdirs = ['11', '12', '01', '02']
    start_time = 520
    end_time = 1700

    copy_files(src_folder, dst_folder, subdirs, start_time, end_time)
