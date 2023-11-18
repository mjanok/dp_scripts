import random

def split_file(input_file, train_ratio, test_ratio):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    random.shuffle(lines)

    total_lines = len(lines)
    train_lines = int(total_lines * train_ratio)
    test_lines = int(total_lines * test_ratio)

    train_data = lines[:train_lines]
    test_data = lines[train_lines : train_lines + test_lines]
    test_after_data = lines[train_lines + test_lines:]

    with open('data/train.txt', 'w') as train_file:
        train_file.writelines(train_data)

    with open('data/test.txt', 'w') as test_file:
        test_file.writelines(test_data)

    with open('data/test_after.txt', 'w') as test_after_file:
        test_after_file.writelines(test_after_data)

    print(f'Split complete. Train data: {len(train_data)} lines, Test data: {len(test_data)} lines, Test After data: {len(test_after_data)} lines.')

# Provide the path to the input text file and the desired ratios for train, test, and test_after
input_file = 'data/image_list.txt'  # Replace with the path to your input file
train_ratio = 0.7  # Set your desired train ratio (e.g., 0.6 for a 60% train split)
test_ratio = 0.1  # Set your desired test ratio (e.g., 0.2 for a 20% test split)

split_file(input_file, train_ratio, test_ratio)
