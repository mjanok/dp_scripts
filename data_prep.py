import subprocess
import time

# List of Python scripts to execute
scripts = [
    "xml_conversion.py",
    "numbering.py",
    "xml_next_conversion.py",
    "presplit.py",
    "split.py"
]

# Function to execute a Python script and measure its execution time
def execute_script(script_name):
    start_time = time.time()
    subprocess.call(["python", script_name])
    end_time = time.time()
    return end_time - start_time

# Store execution times for each script
execution_times = []

# Execute each script and measure execution time
for script in scripts:
    print(f"Executing {script}...")
    execution_time = execute_script(script)
    execution_times.append((script, execution_time))
    print(f"{script} executed in {execution_time:.2f} seconds")

# Calculate total execution time
total_execution_time = sum(execution_time for _, execution_time in execution_times)
print(f"Total execution time for all scripts: {total_execution_time:.2f} seconds")
