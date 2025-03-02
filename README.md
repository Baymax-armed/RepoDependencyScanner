# Dependency Checker and Repository Dependency Extractor

This project provides two main tools:
1. **Dependency Checker**: A GUI-based tool to check the latest versions of dependencies listed in a JSON file.
2. **Repository Dependency Extractor**: A tool to scan a repository, extract dependencies, and generate a JSON report.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Dependency Checker](#dependency-checker)
   - [Repository Dependency Extractor](#repository-dependency-extractor)
4. [Output](#output)
5. [License](#license)

---

## Features

####################### Dependency Checker ############################
- **Upload JSON File**: Load a JSON file containing dependency information.
- **Check Latest Versions**: Automatically fetches the latest version of each dependency from NuGet and PyPI.
- **Sorting**: Sort the table by clicking on column headers.
- **Search**: Search for specific dependencies or files in the table.
- **Version Comparison**: Highlights outdated dependencies and suggests the latest version.

####################### Repository Dependency Extractor ############################
- **Scan Repository**: Scans a repository using ScanCode Toolkit to extract dependency information.
- **Extract Binaries**: Finds all DLLs, EXEs, and other binary files in the repository.
- **Generate JSON Report**: Combines ScanCode output with extracted binaries into a final JSON file.

---

## Installation

### Prerequisites
- Python 3.x
- ScanCode Toolkit (for Repository Dependency Extractor)
- Required Python packages: `requests`, `tkinter`

### Steps ###
1. Clone the repository:
   ```bash
   git clone https://github.com/Baymax-armed/RepoDependencyScanner.git
   cd DependencyChecker

2. Install the required Python packages:
   ```bash
   pip install requests
   pip install requests tkinter

3. Download and set up ScanCode Toolkit (for Repository Dependency Extractor):

   i.Download ScanCode

   ii.Extract it and note the path to scancode.bat

## Usage

### Dependency Checker
1. Run the dependency_checker.py script:
```bash
python dependency_checker.py
```
2. Click on Upload JSON File to load a JSON file containing dependency information.

3. The tool will display the dependencies, their current versions, and the latest available versions.

4. Use the Search bar to filter dependencies or click on column headers to sort the table.

### Repository Dependency Extractor

   1. Run the repo_dependency_extractor.py script:
   ```bash
   python repo_dependency_extractor.py
   ```
   2. Enter the path to your repository when prompted.

3. The tool will:

   i. Scan the repository using ScanCode Toolkit.

   ii. Extract all binaries (DLLs, EXEs, etc.).

   iii.Generate a final JSON report (dependencies_report.json).


## Output

### Dependency Checker
   1. The tool displays a table with the following columns:

      i. File Path: Path to the file in the repository.

      ii. License: Detected license of the file.

      iii. Copyright: Copyright information.

      iv. Package Name: Name of the dependency.

      v. Current Version: Installed version of the dependency.

      vi. CVE: CVE ID if any vulnerabilities are detected.

      vii. Update to this Version: Suggests the latest version if the dependency is outdated.

### Repository Dependency Extractor

#### The tool generates a JSON file (dependencies_report.json) with the following structure:

```bash
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
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
