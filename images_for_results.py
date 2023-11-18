import os
import shutil

def copy_files(src_folder, dst_folder):
    for root,dirs,files in os.walk(src_folder):
        if dirs in subdirs:
            last_dir = os.path.basename(root)
            src_path = os.path.join(src_folder,dirs)
            dst_path = os.path.join(dst_folder)
            if last_dir in range(start_time, end_time + 1):
                for filename in files:
                    src_file = os.path.join(src_path, filename)
                    dst_file = os.path.join(dst_path, filename)
                    shutil.copy(src_file, dst_file)


src_folder = '/data/img'
dst_folder = '/inference/images'
subdirs = ['11', '12', '01','02']
start_time = 520
end_time = 1700

if __name__ == "__main__":
    copy_files(src_folder, dst_folder)
