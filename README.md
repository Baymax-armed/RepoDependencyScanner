Dependency Checker and Repository Dependency Extractor
This project provides two main tools:

Dependency Checker: A GUI-based tool to check the latest versions of dependencies listed in a JSON file.

Repository Dependency Extractor: A tool to scan a repository, extract dependencies, and generate a JSON report.

Table of Contents
Features

Installation

Usage

Dependency Checker

Repository Dependency Extractor

Output

Contributing

License

Features
Dependency Checker
Upload JSON File: Load a JSON file containing dependency information.

Check Latest Versions: Automatically fetches the latest version of each dependency from NuGet and PyPI.

Sorting: Sort the table by clicking on column headers.

Search: Search for specific dependencies or files in the table.

Version Comparison: Highlights outdated dependencies and suggests the latest version.

Repository Dependency Extractor
Scan Repository: Scans a repository using ScanCode Toolkit to extract dependency information.

Extract Binaries: Finds all DLLs, EXEs, and other binary files in the repository.

Generate JSON Report: Combines ScanCode output with extracted binaries into a final JSON file.

Installation
Prerequisites
Python 3.x

ScanCode Toolkit (for Repository Dependency Extractor)

Required Python packages: requests, tkinter

Steps
Clone the repository:

bash
Copy
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install the required Python packages:

bash
Copy
pip install requests
Download and set up ScanCode Toolkit (for Repository Dependency Extractor):

Download ScanCode from here.

Extract it and note the path to scancode.bat.

Usage
Dependency Checker
Run the dependency_checker.py script:

bash
Copy
python dependency_checker.py
Click on Upload JSON File to load a JSON file containing dependency information.

The tool will display the dependencies, their current versions, and the latest available versions.

Use the Search bar to filter dependencies or click on column headers to sort the table.

Repository Dependency Extractor
Run the repo_dependency_extractor.py script:

bash
Copy
python repo_dependency_extractor.py
Enter the path to your repository when prompted.

The tool will:

Scan the repository using ScanCode Toolkit.

Extract all binaries (DLLs, EXEs, etc.).

Generate a final JSON report (dependencies_report.json).

Output
Dependency Checker
The tool displays a table with the following columns:

File Path: Path to the file in the repository.

License: Detected license of the file.

Copyright: Copyright information.

Package Name: Name of the dependency.

Current Version: Installed version of the dependency.

CVE: CVE ID if any vulnerabilities are detected.

Update to this Version: Suggests the latest version if the dependency is outdated.

Repository Dependency Extractor
The tool generates a JSON file (dependencies_report.json) with the following structure:

{
  "files": [
    {
      "path": "path/to/file",
      "license_detections": [{"license_expression": "MIT"}],
      "copyrights": [{"statement": "Copyright 2023"}],
      "package_data": [{"name": "package-name", "version": "1.0.0"}],
      "vulnerabilities": [{"cve_id": "CVE-2023-1234"}]
    }
  ],
  "binaries": [
    {
      "file_name": "example.dll",
      "file_path": "path/to/example.dll"
    }
  ]
}
Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
ScanCode Toolkit for dependency scanning.

NuGet and PyPI for package version information.

