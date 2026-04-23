import base64
import os

html_path = "/Users/guilhermerossi/Documents/ai dw/data-savings/index.html"
logo_path = "/Users/guilhermerossi/Documents/ai dw/data-savings/logo.avif"
output_path = "/Users/guilhermerossi/Documents/ai dw/download/data-savings.html"

# Read HTML
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Read logo and encode
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        logo_data = f.read()
        logo_base64 = base64.b64encode(logo_data).decode("utf-8")
        logo_mime = "image/avif"
        logo_uri = f"data:{logo_mime};base64,{logo_base64}"
        
        # Replace occurrences
        # Using simple replace for src="logo.avif"
        content = content.replace('src="logo.avif"', f'src="{logo_uri}"')

# Ensure download directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write output
with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully created single-file HTML at {output_path}")
