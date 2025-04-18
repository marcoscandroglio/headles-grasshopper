# Grasshopper-as-Code

This project explores a code-first approach to generating Grasshopper definitions using Python. Instead of creating parametric models manually within the Grasshopper UI, this workflow allows logic and parameters to be externalized, versioned, and instantiated from code.

## Overview

The system works by treating Grasshopper's `.ghx` format as a lightweight domain-specific language (DSL) for parametric design. A Python script reads a `.ghx` template file, locates specific components (such as sliders), and updates their values based on a dictionary of named inputs.

This enables batch creation of parametric design variants, integration with external systems, and the ability to reuse Grasshopper logic in a modular and scalable way.

## Features

- Modify number slider values in `.ghx` files programmatically
- Maintain GUI compatibility with Grasshopper for visualization and debugging
- Support for expanding to include component wiring and templating
- Works with any `.ghx` file that uses clearly named components

## Use Case Examples

- Automatically generating design variants for simulation or fabrication
- Integrating parametric logic with optimization algorithms or machine learning agents
- Enabling code-driven control of Grasshopper definitions through CLI or API interfaces
- Creating a logic-first infrastructure for architectural or engineering design systems

## How It Works

1. A valid Grasshopper `.ghx` file is created with named sliders (e.g., `x_spacing`, `y_spacing`)
2. The Python script parses this file, finds the matching components, and updates their values
3. A modified `.ghx` file is saved, which can be opened in Grasshopper as usual

## Requirements

- Python 3.8+
- No external libraries required (uses Python's built-in `xml.etree.ElementTree`)
- Rhino and Grasshopper (for generating `.ghx` templates and testing output)

## Getting Started

1. Open Grasshopper and create a `.ghx` file with named sliders
2. Save the file (File > Save As > choose `.ghx`)
3. Run the Python script with your desired parameter values
4. Open the generated `.ghx` in Grasshopper to inspect or use the updated model

## Future Directions

- Wiring components dynamically
- Creating reusable component templates
- Building a high-level syntax for describing Grasshopper logic in Python
- Integration with Rhino.Compute for server-side geometry generation

## Disclaimer

This project is an independent exploration and is not affiliated with or endorsed by McNeel & Associates. Grasshopper is a closed-source system. This tool works by interfacing with its XML `.ghx` format in a way that preserves compatibility without reverse-engineering compiled binaries.
