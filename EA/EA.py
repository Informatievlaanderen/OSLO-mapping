import win32com.client

def find_diagram(package, diagram_name):
    # Search for the diagram in the current package
    for diagram in package.Diagrams:
        if diagram.Name == diagram_name:
            return diagram

    # If not found, search in sub-packages
    for sub_package in package.Packages:
        found_diagram = find_diagram(sub_package, diagram_name)
        if found_diagram is not None:
            return found_diagram

    return None

def main():
    # Path to your EA project file
    ea_file_path = "C:/Users/samue/Downloads/OSLO-BodemEnOndergrond-AP.EAP"

    try:
        # Create a new instance of EA.Repository
        repository = win32com.client.Dispatch("EA.Repository")

        # Open the EA project file
        repository.OpenFile(ea_file_path)
        print("Opened EA file:", ea_file_path)

        # Accessing the root model
        models = repository.Models
        root_model = models.GetAt(0)
        print("Root Model Name:", root_model.Name)

        # Find the diagram
        diagram_name = "OSLO-SensorenEnBemonstering"
        diagram = find_diagram(root_model, diagram_name)
        
        if diagram is not None:
            image_path = "C:\\path\\to\\your\\directory\\diagram.png"  # Replace with your actual path

            print("Opened diagram:", diagram_name)
            print("Diagram ID:", diagram.DiagramID)
            print("Image path:", image_path)
            print("Image type:", 1)  # Assuming you're exporting as PNG


            # Export the diagram to an image
            result = repository.PutDiagramImageToFile(diagram.DiagramID, image_path, 1)
            if result:
                print("Diagram exported as image:", image_path)
            else:
                print("Failed to export diagram as image")
        else:
            print("Diagram not found:", diagram_name)

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the EA project file
        repository.CloseFile()
        print("Closed EA file.")

if __name__ == "__main__":
    main()