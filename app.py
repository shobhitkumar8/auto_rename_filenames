# import os
# import xml.etree.ElementTree as ET

# def rename_file_using_xml(xml_file_path):
#     # Parse the XML file
#     tree = ET.parse(xml_file_path)
#     root = tree.getroot()

#     # Extract the original and exported file names
#     original_file_name = root.find('original').text
#     exported_file_name = root.find('name').text

#     # Check if the exported file exists
#     if os.path.exists(exported_file_name):
#         # Rename the exported file to the original file name
#         os.rename(exported_file_name, original_file_name)
#         print(f"File renamed from {exported_file_name} to {original_file_name}")
#     else:
#         print(f"Exported file {exported_file_name} does not exist.")

# # Usage example
# xml_file_path = 'files.xml'  # Path to your XML file
# rename_file_using_xml(xml_file_path)


# import os
# import xml.etree.ElementTree as ET

# def rename_file_using_xml(xml_file_path):
#     # Parse the XML file
#     tree = ET.parse(xml_file_path)
#     root = tree.getroot()

#     # Try to find the 'original' and 'name' elements
#     original_element = root.find('.//original')
#     exported_element = root.find('name')

#     # Check if both elements are found
#     if original_element is None or exported_element is None:
#         print("Error: Missing 'original' or 'name' element in the XML file.")
#         return

#     # Extract the file names
#     original_file_name = original_element.text
#     exported_file_name = exported_element.text

#     # Check if the exported file exists
#     if os.path.exists(exported_file_name):
#         # Rename the exported file to the original file name
#         os.rename(exported_file_name, original_file_name)
#         print(f"File renamed from {exported_file_name} to {original_file_name}")
#     else:
#         print(f"Exported file {exported_file_name} does not exist.")

# # Usage example
# xml_file_path = 'files.xml'  # Path to your XML file
# rename_file_using_xml(xml_file_path)





# import os
# import xml.etree.ElementTree as ETree

# def renamefiles(xml_path):
#     # Parse the XML file
#     tree = ETree.parse(xml_path)
#     root = tree.getroot()

#     # Finding the <file> element
#     file_element = root.find('file')

#     # Checking if the <file> element exists and has the required attributes
#     if file_element is not None:
#         original_name = file_element.get('original')
#         exported_name = file_element.get('name')

        
#         if original_name and exported_name:
            
#             if os.path.exists(exported_name):
#                 # Renaming the exported file to the original file name
#                 os.rename(exported_name, original_name)
#                 print(f"File renamed from {exported_name} to {original_name}")
#             else:
#                 print(f"Exported file {exported_name} does not exist.")
#         else:
#             print("Error: 'original' or 'name' attribute is missing in the <file> element.")
#     else:
#         print("Error: <file> element not found in the XML file.")


# xml_path = 'files 1.xml'  # Path to XML file
# renamefiles(xml_path)



# import os
# import xml.etree.ElementTree as ET

# def rename_files_in_directory(parent_directory):
#     # Loop through all subdirectories in the parent directory
#     for subdir, dirs, files in os.walk(parent_directory):
#         # Look for the XML file in the current subdirectory
#         for file in files:
#             if file.endswith('.xml'):
#                 xml_file_path = os.path.join(subdir, file)

#                 print(f"Processing XML: {xml_file_path}")  # Debugging

#                 # Parse the XML file
#                 tree = ET.parse(xml_file_path)
#                 root = tree.getroot()

#                 # Iterate over all <file> elements in the XML
#                 for file_element in root.findall('file'):
#                     original_file_name = file_element.get('original')
#                     exported_file_name = file_element.get('name')

#                     # Ensure both 'original' and 'name' attributes exist
#                     if original_file_name and exported_file_name:
#                         # Full path of the exported file
#                         exported_file_path = os.path.join(subdir, exported_file_name)
#                         original_file_path = os.path.join(subdir, original_file_name)

#                         # Print paths for debugging
#                         print(f"Exported file path: {exported_file_path}")
#                         print(f"Original file path: {original_file_path}")

#                         # Check if the exported file exists in the current folder
#                         if os.path.exists(exported_file_path):
#                             # Rename the exported file to the original file name
#                             os.rename(exported_file_path, original_file_path)
#                             print(f"File renamed from {exported_file_name} to {original_file_name} in {subdir}")
#                         else:
#                             print(f"Exported file {exported_file_name} does not exist in {subdir}.")
#                     else:
#                         print("Error: 'original' or 'name' attribute is missing in a <file> element in the XML.")

# # Usage example
# parent_directory = r'C:\Users\shobkuma\OneDrive-Capgemini\Desktop\002'  # Specify your parent directory path here
# rename_files_in_directory(parent_directory)



# import os
# import xml.etree.ElementTree as ET

# def rename_files_in_directory(parent_directory):
#     # Loop through all subdirectories in the parent directory
#     for subdir, dirs, files in os.walk(parent_directory):
#         print(f"Checking folder: {subdir}")  # Debugging: Check which folder is being processed
#         # Look for the XML file in the current subdirectory
#         for file in files:
#             if file.endswith('.xml'):
#                 xml_file_path = os.path.join(subdir, file)

#                 print(f"Processing XML: {xml_file_path}")  # Debugging: XML file found

#                 # Parse the XML file
#                 try:
#                     tree = ET.parse(xml_file_path)
#                     root = tree.getroot()
#                 except ET.ParseError as e:
#                     print(f"Error parsing XML file {xml_file_path}: {e}")
#                     continue  # Skip this file if there's an error parsing it

#                 # Iterate over all <file> elements in the XML
#                 for file_element in root.findall('file'):
#                     original_file_name = file_element.get('original')
#                     exported_file_name = file_element.get('name')

#                     # Ensure both 'original' and 'name' attributes exist
#                     if original_file_name and exported_file_name:
#                         # Full path of the exported file
#                         exported_file_path = os.path.join(subdir, exported_file_name)
#                         original_file_path = os.path.join(subdir, original_file_name)

#                         # Print paths for debugging
#                         print(f"Exported file path: {exported_file_path}")
#                         print(f"Original file path: {original_file_path}")

#                         # Check if the exported file exists in the current folder
#                         if os.path.exists(exported_file_path):
#                             try:
#                                 # Rename the exported file to the original file name
#                                 os.rename(exported_file_path, original_file_path)
#                                 print(f"File renamed from {exported_file_name} to {original_file_name} in {subdir}")
#                             except PermissionError as pe:
#                                 print(f"Permission error: {pe}")
#                             except OSError as oe:
#                                 print(f"OS error: {oe}")
#                         else:
#                             print(f"Exported file {exported_file_name} does not exist in {subdir}.")
#                     else:
#                         print("Error: 'original' or 'name' attribute is missing in a <file> element in the XML.")

# # Usage example
# parent_directory = r'C:\Users\shobkuma\OneDrive-Capgemini\Desktop\002'  # Specify your parent directory path here
# rename_files_in_directory(parent_directory)


import os
import xml.etree.ElementTree as ET

def rename_files_in_directory(parent_directory):
    # Debugging: Check if the directory exists
    if not os.path.exists(parent_directory):
        print(f"Error: Parent directory {parent_directory} does not exist!")
        return
    
    print(f"Parent directory: {parent_directory}")  # Confirming the parent directory

    # Loop through all subdirectories in the parent directory
    for subdir, dirs, files in os.walk(parent_directory):
        print(f"Checking folder: {subdir}")  # Debugging: Check which folder is being processed
        print(f"Files: {files}")             # Debugging: Check what files are in the current directory
        print(f"Subdirectories: {dirs}")     # Debugging: Check subdirectories in the current directory

        # Look for the XML file in the current subdirectory
        for file in files:
            if file.endswith('.xml'):
                xml_file_path = os.path.join(subdir, file)
                print(f"Processing XML: {xml_file_path}")  # Debugging: XML file found

                # Parse the XML file
                try:
                    tree = ET.parse(xml_file_path)
                    root = tree.getroot()
                except ET.ParseError as e:
                    print(f"Error parsing XML file {xml_file_path}: {e}")
                    continue  # Skip this file if there's an error parsing it

                # Iterate over all <file> elements in the XML
                for file_element in root.findall('file'):
                    original_file_name = file_element.get('original')
                    exported_file_name = file_element.get('name')

                    # Ensure both 'original' and 'name' attributes exist
                    if original_file_name and exported_file_name:
                        # Full path of the exported file
                        exported_file_path = os.path.join(subdir, exported_file_name)
                        original_file_path = os.path.join(subdir, original_file_name)

                        # Print paths for debugging
                        print(f"Exported file path: {exported_file_path}")
                        print(f"Original file path: {original_file_path}")

                        # Check if the exported file exists in the current folder
                        if os.path.exists(exported_file_path):
                            try:
                                # Rename the exported file to the original file name
                                os.rename(exported_file_path, original_file_path)
                                print(f"File renamed from {exported_file_name} to {original_file_name} in {subdir}")
                            except PermissionError as pe:
                                print(f"Permission error: {pe}")
                            except OSError as oe:
                                print(f"OS error: {oe}")
                        else:
                            print(f"Exported file {exported_file_name} does not exist in {subdir}.")
                    else:
                        print("Error: 'original' or 'name' attribute is missing in a <file> element in the XML.")

# Usage example
parent_directory = r''  # Specify your parent directory path here
rename_files_in_directory(parent_directory)

