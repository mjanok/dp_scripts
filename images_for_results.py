import os
import shutil

def copy_files(src_folder, dst_folder, subdirs, start_time, end_time):
    for root, dirs, files in os.walk(src_folder):
        # Check if all subdirs are present
        if root[9:11] in subdirs:
            last_dir = os.path.basename(root)
            time = root[15:19]
            if time.startswith("0"):
                time = int(time.lstrip("0"))
            elif time:
                time = int(time)
            if time in range(start_time, end_time + 1):
                # Get the parent directory (one level up from the last directory)
                parent_dir = os.path.dirname(root)
                src_path = os.path.join(parent_dir, last_dir)

                # Iterate over files in the source directory and copy them to the destination
                for filename in files:
                    src_file = os.path.join(src_path, filename)
                    dst_file = os.path.join(dst_folder, filename)
                    shutil.copy2(src_file, dst_file)


if __name__ == "__main__":
    # Example usage:
    src_folder = 'data/img'
    dst_folder = 'inference/images'
    subdirs = ['11', '12', '01', '02']
    start_time = 520
    end_time = 1700

    copy_files(src_folder, dst_folder, subdirs, start_time, end_time)
