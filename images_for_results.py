import os
import shutil

def copy_files(src_folder, dst_folder, subdirs, start_time, end_time):
    for root, dirs, files in os.walk(src_folder):
        # Check if any subdirectory matches the desired list
        if any(d in subdirs for d in dirs):
            last_dir = os.path.basename(root)
            if last_dir.isdigit() and int(last_dir) in range(start_time, end_time + 1):
                src_path = os.path.join(src_folder, last_dir)
                dst_path = os.path.join(dst_folder, last_dir)

                # Create the destination directory if it doesn't exist
                os.makedirs(dst_path, exist_ok=True)

                # Iterate over files in the source directory and copy them to the destination
                for filename in files:
                    src_file = os.path.join(src_path, filename)
                    dst_file = os.path.join(dst_path, filename)
                    shutil.copy2(src_file, dst_file)

                print(f"Files from {src_path} copied to {dst_path}")

# Example usage:
src_folder = '/data/img'
dst_folder = '/inference/images'
subdirs = ['11', '12', '01', '02']
start_time = 520
end_time = 1700

if __name__ == "__main__":
    copy_files(src_folder, dst_folder, subdirs, start_time, end_time)
