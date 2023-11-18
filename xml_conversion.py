import xml.etree.ElementTree as ET
import os
import csv
import time
import random
#TODO pridať komentare, zhodnotiť potrebu Floating Threshold
DIRa = "data/annot"
DIRi = "data/img"
DEST_DIR = "data/annots_new/"
class_distance_dict = {}
root_dict = {}
start_time = time.time() 
# create dictionary with roots 
for root, dirs, files in os.walk(DIRi):
    for file in files:
        # check if file has .jpg extension
        if file.endswith('.jpg'):
            root_dict[file[24:]] = root
# iterate all xml files and change them

now = 0
for root, dirs, files in os.walk(DIRa):
    # take only the first line of var root
    input = str(root).splitlines()[0]
    for file in files:
        # check if file has .xml extension
        if file.endswith('.xml'):
            # define input file path
            input_file = input + "\\"  + file
            # parse input XML file
            tree = ET.parse(input_file)
            root = tree.getroot()
            # create root element of output XML file
            output_root = ET.Element("annotation")
            # add child elements to root element
            folder = ET.SubElement(output_root, "folder")
            folder.text = "blank"
            filename = ET.SubElement(output_root, "filename")
            path = ET.SubElement(output_root, "path")
            source = ET.SubElement(output_root, "source")
            database = ET.SubElement(source, "database")
            database.text = "Unknown"
            size = ET.SubElement(output_root, "size")
            width = ET.SubElement(size, "width")
            width.text = "1920"
            height = ET.SubElement(size, "height")
            height.text = "1080"
            depth = ET.SubElement(size, "depth")
            depth.text = "3"
            segmented = ET.SubElement(output_root, "segmented")
            segmented.text = "0"

            # find all 'pvr' elements and create 'object' elements in output XML file, filter out not visible objects
            for pvr in root.findall(".//pvrList/x"):
                if pvr.get("isVisible") == "false":
                    continue
                # filter out by point size
                if (int(pvr.get("width"))) <= 10 or (int(pvr.get("height")) <= 10):
                    continue
                object1 = ET.SubElement(output_root, "object")
                name = ET.SubElement(object1, "name")
                name1 = pvr.get("path")
                name2 = name1[76:]
                name2 = name2.split("_")
                name.text = f"{name2[0]}_{name2[1]}_{name2[2]}_{file[22:25]}" 
                class_name = f"{name2[0]}_{name2[1]}_{name2[2]}_{file[22:25]}"
                distance = pvr.get("distance")
                if class_name not in class_distance_dict:
                    class_distance_dict[class_name] = distance
                pose = ET.SubElement(object1, "pose")
                pose.text = "Unspecified"
                truncated = ET.SubElement(object1, "truncated")
                truncated.text = "0"
                difficult = ET.SubElement(object1, "difficult")
                difficult.text = "0"
                bndbox = ET.SubElement(object1, "bndbox")
                xmin = ET.SubElement(bndbox, "xmin")
                xmin.text = str(int(pvr.get("x")) + int(pvr.get("xShift")))
                ymin = ET.SubElement(bndbox, "ymin")
                ymin.text = str(int(pvr.get("y")) + int(pvr.get("yShift")))
                width = ET.SubElement(bndbox, "width")
                width.text = str(int(pvr.get("width")))
                height = ET.SubElement(bndbox, "height")
                height.text = str(int(pvr.get("height")))
            # write output XML file
            for key in root_dict.keys():
                if key[:-5] == file [22:-5]:
                    output_file =  key[:-4] + ".xml"
                    filename.text = "panasonic_fullhd_01-090-" + key
                    path.text = root_dict[key] + "\\" + "panasonic_fullhd_01-090-" + key
                    output_tree = ET.ElementTree(output_root)
                    output_tree.write(DEST_DIR + output_file)
                    if now % 1000 == 0:
                        print ("Created file number: " + str(now))
                    now +=1

csv_file_path = "class_distance.csv"
with open(csv_file_path, mode='w', newline='') as csv_file:
    fieldnames = ["Class_name", "distance", "direction"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # Write the CSV header
    writer.writeheader()

    # Write class names and distances to the CSV file
    for class_name, distance in class_distance_dict.items():
        writer.writerow({"Class_name": class_name, "distance": distance, "direction":class_name[-3:]})
end_time = time.time()  # End timing
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

            

