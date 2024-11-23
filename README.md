# Design Language Documentation

This documentation outlines the usage and functionality of the **Design Language Interpreter**.

## Overview
The Design Language Interpreter allows designers to create visual elements using a simple scripting language. It translates design commands into HTML and CSS for rendering. This language is designed to mimic the workflows of tools like Figma, enabling rapid prototyping directly from code.

## Features
- **Basic Shapes**: Rectangles, circles, ellipses, and lines.
- **Images**: Add images via URLs.
- **Text**: Add styled text with customizable font size and color.
- **Gradients**: Define gradient backgrounds for shapes.
- **Opacity and Positioning**: Customize transparency and absolute positioning.

---

## Installation

To install and use **Design Language**, follow these steps:

### 1. Clone the Repository
```bash
git clone <repository-url>
cd design-language
```

### 2. Install the Package

For local development, install the package in editable mode:
```bash
pip install -e .
```

### 3. Install Dependencies

Ensure that required dependencies are installed:
```bash
pip install -r requirements.txt
```

---

## Usage

Once installed, you can use Design Language in the following way:

### 1. Create a Design Code File
Write your design code in a `.dl` file. For example, create a file named `example.dl` with the following content:

```
FRAME width=800 height=600 color=#f9f9f9
    RECTANGLE width=200 height=100 color=blue position=(50, 50) opacity=0.8
    CIRCLE radius=50 color=red position=(300, 100) opacity=0.6
    LINE length=400 thickness=5 color=green position=(100, 200)
    IMAGE url="https://via.placeholder.com/150" width=150 height=150 position=(400, 300)
    TEXT "Hello, Designers!" size=24 color=black position=(200, 500)
    GRADIENT width=400 height=100 colors=(red,blue,green) position=(200, 350)
END
```

### 2. Run the Interpreter
Use the command-line interface to generate the HTML output:

```bash
python src/parser.py example.dl
```

This will generate an `output.html` file in the current directory.

### 3. View the Output
Open the `output.html` file in any modern web browser to view your design.

---

## Syntax Reference

### Frame
Defines the container for your design.

```
FRAME width=<pixels> height=<pixels> color=<hex_color>
```

Example:
```
FRAME width=800 height=600 color=#f9f9f9
```

### Rectangle
Creates a rectangle with specified dimensions, color, position, and optional opacity.

```
RECTANGLE width=<pixels> height=<pixels> color=<hex_color> position=(<x>,<y>) [opacity=<0-1>]
```

Example:
```
RECTANGLE width=200 height=100 color=blue position=(50, 50) opacity=0.8
```

### Circle
Creates a circle with a specified radius, color, position, and optional opacity.

```
CIRCLE radius=<pixels> color=<hex_color> position=(<x>,<y>) [opacity=<0-1>]
```

Example:
```
CIRCLE radius=50 color=red position=(300, 100) opacity=0.6
```

### Ellipse
Creates an ellipse with specified dimensions, color, position, and optional opacity.

```
ELLIPSE width=<pixels> height=<pixels> color=<hex_color> position=(<x>,<y>) [opacity=<0-1>]
```

Example:
```
ELLIPSE width=150 height=100 color=green position=(200, 150) opacity=0.7
```

### Line
Creates a line with a specified length, thickness, color, position, and optional opacity.

```
LINE length=<pixels> thickness=<pixels> color=<hex_color> position=(<x>,<y>) [opacity=<0-1>]
```

Example:
```
LINE length=400 thickness=5 color=black position=(100, 200)
```

### Image
Adds an image using a URL, with specified dimensions and position.

```
IMAGE url="<image_url>" width=<pixels> height=<pixels> position=(<x>,<y>) [opacity=<0-1>]
```

Example:
```
IMAGE url="https://via.placeholder.com/150" width=150 height=150 position=(400, 300)
```

### Text
Adds text with specified font size, color, position, and optional opacity.

```
TEXT "<text>" size=<pixels> color=<hex_color> position=(<x>,<y>) [opacity=<0-1>]
```

Example:
```
TEXT "Hello, Designers!" size=24 color=black position=(200, 500)
```

### Gradient
Creates a rectangular gradient with specified dimensions, colors, and position.

```
GRADIENT width=<pixels> height=<pixels> colors=(<color1>,<color2>,...) position=(<x>,<y>)
```

Example:
```
GRADIENT width=400 height=100 colors=(red,blue,green) position=(200, 350)
```

---

## Example Design Code
Below is a full example demonstrating the language:

```
FRAME width=800 height=600 color=#f9f9f9
    RECTANGLE width=200 height=100 color=blue position=(50, 50) opacity=0.8
    CIRCLE radius=50 color=red position=(300, 100) opacity=0.6
    LINE length=400 thickness=5 color=green position=(100, 200)
    IMAGE url="https://via.placeholder.com/150" width=150 height=150 position=(400, 300)
    TEXT "Hello, Designers!" size=24 color=black position=(200, 500)
    GRADIENT width=400 height=100 colors=(red,blue,green) position=(200, 350)
END
```

## Output
Run the interpreter to generate an `HTML` file with the visual representation of your design.

---

## How to Use
1. Save your design code in a `.txt` file.
2. Run the Python script provided in the repository.
3. The generated `design_output.html` file will be created in the same directory.
4. Open the file in any web browser to view your design.

---

## Future Improvements
- Support for animations.
- Grouping elements.
- Export to SVG or PNG.
- Improved error handling and syntax validation.

---

Enjoy designing with the **Design Language Interpreter**!
