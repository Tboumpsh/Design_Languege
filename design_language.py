import re

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Design Output</title>
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }}
        .frame {{
            position: relative;
            margin: auto;
            background-color: {background_color};
            width: {frame_width}px;
            height: {frame_height}px;
            overflow: hidden;
            border: 1px solid #ccc;
        }}
        .element {{
            position: absolute;
            opacity: 1;
            transition: all 0.3s ease;
        }}
        .element:hover {{
            transform: scale(1.1);
        }}
    </style>
</head>
<body>
    <div class="frame">
        {content}
    </div>
    <script>
        {scripts}
    </script>
</body>
</html>
"""

def parse_design_code(code):
    frame_width, frame_height, background_color = 600, 400, "#ffffff"
    content = []
    scripts = []

    lines = code.strip().split("\n")
    for line in lines:
        line = line.strip()

        if line.startswith("FRAME"):
            match = re.search(r"width=(\d+)\s+height=(\d+)\s+color=([\w#]+)", line)
            if match:
                frame_width, frame_height, background_color = map(str.strip, match.groups())
                print(f"Frame: width={frame_width}, height={frame_height}, color={background_color}")
                frame_width, frame_height = int(frame_width), int(frame_height)

        elif line.startswith("RECTANGLE"):
            match = re.search(
                r"width=(\d+)\s+height=(\d+)\s+color=([\w#]+)\s+position=\((\d+),\s*(\d+)\)(?:\s+opacity=([\d.]+))?",
                line
            )
            if match:
                width, height, color, x, y, opacity = match.groups()
                print(f"Rectangle: {width}, {height}, {color}, position=({x}, {y}), opacity={opacity}")
                opacity = opacity if opacity else "1"
                content.append(f'<div class="element" style="width: {width}px; height: {height}px; background-color: {color}; left: {x}px; top: {y}px; opacity: {opacity};"></div>')

    return frame_width, frame_height, background_color, "\n".join(content), "\n".join(scripts)

def generate_html(code):
    frame_width, frame_height, background_color, content, scripts = parse_design_code(code)
    html_content = HTML_TEMPLATE.format(
        frame_width=frame_width,
        frame_height=frame_height,
        background_color=background_color,
        content=content,
        scripts=scripts
    )
    print("Generated HTML Content:")
    print(html_content)
    with open("design_output.html", "w") as file:
        file.write(html_content)
    print("HTML file generated: design_output.html")

design_code = """
FRAME width=800 height=600 color=#f9f9f9
    RECTANGLE width=200 height=100 color=blue position=(50, 50) opacity=0.8
    CIRCLE radius=50 color=red position=(300, 100) opacity=0.6
    LINE length=400 thickness=5 color=green position=(100, 200)
    IMAGE url="https://via.placeholder.com/150" width=150 height=150 position=(400, 300)
    TEXT "Hello, Designers!" size=24 color=black position=(200, 500)
    GRADIENT width=400 height=100 colors=(red,blue,green) position=(200, 350)
END
"""

generate_html(design_code)
