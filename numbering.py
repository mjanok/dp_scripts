import os
import shutil
from multiprocessing import Pool

def copy_file(args):
    src, dest = args
    shutil.copy(src, dest)

def find_and_copy_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    file_counter = 1
    file_pairs = []

    for root, _, files in os.walk(src_folder):
        for filename in files:
            if filename.endswith('.jpg'):
                jpg_path = os.path.join(root, filename)
                xml_filename = filename.replace('panasonic_fullhd_01-090-', '').replace('jpg', 'xml').replace('img', 'annots_new')
                xml_path = os.path.join(annots_folder, xml_filename)
                if os.path.exists(xml_path):
                    new_jpg_name = f"{file_counter}.jpg"
                    new_xml_name = f"{file_counter}.xml"
                    dest_jpg_path = os.path.join(dest_folder, new_jpg_name)
                    dest_xml_path = os.path.join(dest_folder, new_xml_name)
                    file_pairs.append((jpg_path, dest_jpg_path))
                    file_pairs.append((xml_path, dest_xml_path))
                    file_counter += 1


    pool = Pool(processes=os.cpu_count())
    pool.map(copy_file, file_pairs)
    pool.close()
    pool.join()

if __name__ == "__main__":
    img_folder = "data/img"  
    annots_folder = "data/annots_new" 
    data_folder = "data/obj"  # Destination folder
    find_and_copy_files(img_folder, data_folder)
    find_and_copy_files(annots_folder, data_folder)
