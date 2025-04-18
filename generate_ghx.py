import xml.etree.ElementTree as ET
import uuid
import os

# Helper to create new GUIDs for GH components
def new_guid():
    return str(uuid.uuid4()).upper()

# Helper to create a slider component XML block
def create_slider_xml(name, value, min_val, max_val, x, y):
    slider_id = new_guid()
    obj = ET.Element("object", name="Slider", nickname=name, guid=slider_id, x=str(x), y=str(y))

    # Slider configuration
    slider_chunk = ET.SubElement(obj, "chunk", name="Slider")
    ET.SubElement(slider_chunk, "item", name="Value", type="System.Double").text = str(value)
    ET.SubElement(slider_chunk, "item", name="Minimum", type="System.Double").text = str(min_val)
    ET.SubElement(slider_chunk, "item", name="Maximum", type="System.Double").text = str(max_val)

    return obj

# Helper to create a rectangle component (placeholder block)
def create_rectangle_xml(name, x, y):
    rect_id = new_guid()
    obj = ET.Element("object", name="Rectangle", nickname=name, guid=rect_id, x=str(x), y=str(y))

    # Minimal placeholder structure
    rect_chunk = ET.SubElement(obj, "chunk", name="Rectangle")
    ET.SubElement(rect_chunk, "item", name="SomeValue", type="System.String").text = "Placeholder"

    return obj

# Main function to generate a minimal GHX file
def generate_minimal_ghx(output_path):
    root = ET.Element("archive", version="1.0")
    doc = ET.SubElement(root, "gh_document")

    # Create and append two sliders
    slider1 = create_slider_xml("x_spacing", value=5.0, min_val=1.0, max_val=20.0, x=100, y=100)
    slider2 = create_slider_xml("y_spacing", value=5.0, min_val=1.0, max_val=20.0, x=100, y=200)
    doc.extend([slider1, slider2])

    # Create and append rectangle placeholder
    rectangle = create_rectangle_xml("grid_rect", x=300, y=150)
    doc.append(rectangle)

    # Write to output file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tree = ET.ElementTree(root)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)

# Generate file
output_file = "C:/Users/Marco Scandroglio/Desktop/GaC/generated_from_scratch.ghx"
generate_minimal_ghx(output_file)

print(f".ghx file created at: {output_file}")
