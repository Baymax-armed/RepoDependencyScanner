import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import requests

def get_latest_version(package_name):
    """ Check latest version from NuGet & PyPI """
    if not package_name or package_name == "N/A":
        return "N/A"
    
    try:
        # Try NuGet first (for .NET DLLs)
        nuget_url = f"https://api.nuget.org/v3-flatcontainer/{package_name.lower()}/index.json"
        response = requests.get(nuget_url, timeout=10)  # Increased timeout to 10 seconds
        if response.status_code == 200:
            try:
                versions = response.json().get("versions", [])
                if versions:
                    return versions[-1]  # Latest version
            except json.JSONDecodeError:
                # If NuGet returns invalid JSON, skip to PyPI
                pass

        # Try PyPI (for Python packages)
        pypi_url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(pypi_url, timeout=10)  # Increased timeout to 10 seconds
        if response.status_code == 200:
            try:
                return response.json().get("info", {}).get("version", "N/A")
            except json.JSONDecodeError:
                # If PyPI returns invalid JSON, return "N/A"
                return "N/A"
        
    except requests.exceptions.RequestException:
        # If any network error occurs, return "N/A"
        return "N/A"
    
    return "N/A"  # If no version found

def load_json():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print("✅ JSON Loaded Successfully")
            print("🔍 Checking installed & latest versions...")
            display_data(data)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load JSON: {e}")

def display_data(data):
    for row in tree.get_children():
        tree.delete(row)
    
    if "files" not in data or not isinstance(data["files"], list):
        messagebox.showerror("Error", "Invalid JSON format! No 'files' key found.")
        return
    
    for file in data["files"]:
        file_name = file.get("path", "N/A")  
        license_info = (
            file.get("license_detections", [{}])[0].get("license_expression", "N/A")
            if file.get("license_detections") else "N/A"
        )
        copyright_info = (
            file.get("copyrights", [{}])[0].get("statement", "N/A")
            if file.get("copyrights") else "N/A"
        )

        package_data = file.get("package_data", [])
        if package_data and isinstance(package_data, list) and len(package_data) > 0:
            package_name = package_data[0].get("name", "N/A")
            current_version = package_data[0].get("version", "N/A")
        else:
            package_name = "N/A"
            current_version = "N/A"

        vulnerabilities = file.get("vulnerabilities", [])
        cve = vulnerabilities[0].get("cve_id", "N/A") if vulnerabilities else "N/A"

        # Fetch latest version from the internet
        latest_version = get_latest_version(package_name)

        # Compare versions (Only show update if newer version exists)
        if latest_version != "N/A" and current_version != "N/A" and latest_version != current_version:
            update_version = latest_version
        else:
            update_version = "Up-to-date ✅"

        tree.insert("", "end", values=(file_name, license_info, copyright_info, package_name, current_version, cve, update_version))

# Initialize Tkinter window before using tree
root = tk.Tk()
root.title("Dependency Checker")
root.geometry("1200x500")

# Add UI elements
tk.Button(root, text="Upload JSON File", command=load_json).pack(pady=10)

# Search bar
search_frame = tk.Frame(root)
search_frame.pack(pady=10)
search_entry = tk.Entry(search_frame, width=50)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", command=lambda: search_tree(search_entry.get())).pack(side=tk.LEFT)

# Define tree table
columns = ("File Path", "License", "Copyright", "Package Name", "Current Version", "CVE", "Update to this Version")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Add column headings and enable sorting
for col in columns:
    tree.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tree, _col, False))
    tree.column(col, width=160)

# Add vertical scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

tree.pack(expand=True, fill="both")

# Function to sort treeview columns
def treeview_sort_column(tv, col, reverse):
    data = [(tv.set(child, col), child) for child in tv.get_children()]
    data.sort(reverse=reverse)

    for index, (val, child) in enumerate(data):
        tv.move(child, "", index)

    tv.heading(col, command=lambda _col=col: treeview_sort_column(tv, _col, not reverse))

# Function to search treeview
def search_tree(search_term):
    search_term = search_term.lower()
    for child in tree.get_children():
        if any(search_term in str(tree.set(child, col)).lower() for col in columns):
            tree.selection_set(child)
            tree.focus(child)
        else:
            tree.selection_remove(child)

# Run Tkinter loop
root.mainloop()