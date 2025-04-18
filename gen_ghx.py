import xml.etree.ElementTree as ET

def update_ghx_sliders(input_path, output_path, updated_values):
    tree = ET.parse(input_path)
    root = tree.getroot()
    found_updates = 0

    def_objects = root.find(".//chunk[@name='DefinitionObjects']")
    if def_objects is None:
        print("❌ Could not find DefinitionObjects section.")
        return

    print("🔍 Found DefinitionObjects. Looking for slider Objects...")

    for obj_chunk in def_objects.findall(".//chunk[@name='Object']"):
        # Use recursive search for the Container chunk
        container_chunks = obj_chunk.findall(".//chunk[@name='Container']")
        for container in container_chunks:
            nickname_item = container.find(".//item[@name='NickName']")
            if nickname_item is None:
                continue

            nickname = nickname_item.text.strip()
            print(f"➡ Found component with nickname: {nickname}")

            if nickname in updated_values:
                slider_chunk = container.find(".//chunk[@name='Slider']")
                if slider_chunk is not None:
                    value_item = slider_chunk.find(".//item[@name='Value']")
                    if value_item is not None:
                        old_value = value_item.text
                        new_value = str(updated_values[nickname])
                        value_item.text = new_value
                        found_updates += 1
                        print(f"✔ Updated slider '{nickname}': {old_value} → {new_value}")
                    else:
                        print(f"⚠ No Value item in slider chunk for {nickname}.")
                else:
                    print(f"⚠ No Slider chunk found for {nickname}.")
            else:
                print(f"✖ Nickname '{nickname}' not in updated_values.")

    if found_updates == 0:
        print("⚠ Still no sliders updated. Try checking case sensitivity or file save format.")
    else:
        print(f"✅ Updated {found_updates} slider(s).")

    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    print(f"📁 Saved updated file: {output_path}")

# Example usage
if __name__ == "__main__":
    input_file = "C:/Users/Marco Scandroglio/Desktop/GaC/base_template_3D.ghx"
    output_file = "C:/Users/Marco Scandroglio/Desktop/GaC/generated_output.ghx"

    updated_values = {
        "x_spacing": 14.0,
        "y_spacing": 9.25,
        "z_spacing": 17.7
    }

    update_ghx_sliders(input_file, output_file, updated_values)
