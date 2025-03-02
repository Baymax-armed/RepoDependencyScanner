import json
import os
import subprocess
from pathlib import Path

def scan_repo(repo_path, output_json):
    """
    Scans the repository using ScanCode Toolkit and extracts dependencies, DLLs, and binary files.
    """
    print("Scanning repository...")
    scan_command = [
    "D:\\scancode-toolkit-develop\\scancode.bat",
    "--package", "--json", output_json, repo_path,
    "--processes", "4", "--license", "--copyright", "--classify"
]

    subprocess.run(scan_command, check=True)
    print(f"Scan completed. Results saved in {output_json}")

def extract_binaries(repo_path):
    """
    Finds all DLLs, EXEs, and other binaries in the repository.
    """
    binaries = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith((".dll", ".exe", ".so", ".bin", ".a", ".lib")):
                binaries.append({
                    "file_name": file,
                    "file_path": os.path.join(root, file)
                })
    return binaries

def generate_final_json(scan_result, repo_path, output_json):
    """
    Combines ScanCode output with extracted binaries and saves the final JSON.
    """
    with open(scan_result, "r", encoding="utf-8") as f:
        scan_data = json.load(f)
    
    binaries = extract_binaries(repo_path)
    scan_data["binaries"] = binaries
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(scan_data, f, indent=4)
    print(f"Final JSON file generated: {output_json}")

def main():
    repo_path = input("Enter the path to your repository: ")
    output_json = "dependencies_report.json"
    scan_result = "scan_result.json"
    
    scan_repo(repo_path, scan_result)
    generate_final_json(scan_result, repo_path, output_json)

if __name__ == "__main__":
    main()
