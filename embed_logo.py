import base64
import os

html_path = "/Users/guilhermerossi/Documents/AI_DW_Workflow/index-dsa.html"
image_path = "/Users/guilhermerossi/Documents/AI_DW_Workflow/Imagens/Logo IDR.png"

with open(image_path, "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode('utf-8')

with open(html_path, "r") as f:
    content = f.read()

target = '<img src="./Imagens/Logo IDR.png" alt="International Data Reserve">'
replacement = f'<img src="data:image/png;base64,{img_base64}" alt="International Data Reserve">'

new_content = content.replace(target, replacement)

with open(html_path, "w") as f:
    f.write(new_content)

print("Successfully replaced image with base64 in index-dsa.html")
