import os
import xml.etree.ElementTree as ET
import csv
import pandas as pd

def extract_names_from_xml(xml_folder):
    unique_names = set()

    for filename in os.listdir(xml_folder):
        if filename.endswith('.xml'):
            xml_path = os.path.join(xml_folder, filename)
            
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                for obj in root.findall('.//object'):
                    name = obj.find('name').text
                    unique_names.add(name)
            except ET.ParseError as e:
                print(f"Error parsing {xml_path}: {e}")

    return list(unique_names)

def convert_xml_to_txt(xml_folder, output_folder, name_dict):
    for filename in os.listdir(xml_folder):
        if filename.endswith('.xml'):
            xml_path = os.path.join(xml_folder, filename)
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(output_folder, txt_filename)
            
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                with open(txt_path, 'w') as txt_file:
                    for obj in root.findall('.//object'):
                        name = obj.find('name').text
                        if name in name_dict:
                            name_id = name_dict[name]
                            bbox = obj.find('bndbox')
                            xmin = float(bbox.find('xmin').text)
                            ymin = float(bbox.find('ymin').text)
                            xmax = float(bbox.find('xmin').text) + float(bbox.find('width').text)
                            ymax = float(bbox.find('ymin').text) + float(bbox.find('height').text)
                            width = 1920  # Image width
                            height = 1080  # Image height
                            x_center = (xmin + xmax) / (2 * width)
                            y_center = (ymin + ymax) / (2 * height)
                            rel_width = (xmax - xmin) / width
                            rel_height = (ymax - ymin) / height
                            txt_file.write(f"{name_id} {x_center:.6f} {y_center:.6f} {rel_width:.6f} {rel_height:.6f}\n")
                os.remove(xml_path)
            except ET.ParseError as e:
                print(f"Error parsing {xml_path}: {e}")

def save_name_dict_to_csv(name_dict, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for name, id in name_dict.items():
            writer.writerow({'Name': name, 'ID': id})

if __name__ == "__main__":
    xml_folder = "data/obj"  
    output_folder = "data/obj"   
    unique_names = extract_names_from_xml(xml_folder)
    
    name_dict = {name: idx for idx, name in enumerate(unique_names)}
    print(name_dict)
    
    # Save name_dict to CSV
    csv_filename = "classes.csv"
    save_name_dict_to_csv(name_dict, csv_filename)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    convert_xml_to_txt(xml_folder, output_folder, name_dict)
  
    # Merge csv and text file
    classes_df = pd.read_csv('classes.csv')
    class_distance_df = pd.read_csv('class_distance.csv')
    merged_df = pd.merge(classes_df, class_distance_df, left_on=['Name'], right_on=['Class_name'], how='inner')
    merged_df = merged_df.drop(columns=['Name', 'Class_name'])
    merged_df.to_csv('class_info.csv', index=False)


    
