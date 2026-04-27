import re
import os

filepath = '/Users/guilhermerossi/Documents/AI_DW_Workflow/data-savings-prototype-v5.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract everything before the first surface
head_match = re.search(r'(<!DOCTYPE html>.*?<div class="canvas" id="canvas">)', content, re.DOTALL)
head_part = head_match.group(1)

# Remove the chrome nav
head_part = re.sub(r'<!-- ===+.*?CHROME — minimal surface switcher.*?</div>\s*</div>\s*', '', head_part, flags=re.DOTALL)

# Extract surfaces
surface_ad_match = re.search(r'(<!-- Surface 1a · Ad \(WITH\) -->.*?)(?=<!-- Surface 2 · Data Savings Act -->)', content, re.DOTALL)
surface_act_match = re.search(r'(<!-- Surface 2 · Data Savings Act -->.*?)(?=<!-- Surface 3a · DrumWave \(WITH\) -->)', content, re.DOTALL)
surface_dw_match = re.search(r'(<!-- Surface 3a · DrumWave \(WITH\) -->.*?)(?=<!-- Surface 4 · IDR -->)', content, re.DOTALL)
surface_idr_match = re.search(r'(<!-- Surface 4 · IDR -->.*?)(?=</div>\s*<!-- annotations removed -->)', content, re.DOTALL)

# Extract everything after the last surface
footer_match = re.search(r'(</div>\s*<!-- annotations removed -->.*?</html>)', content, re.DOTALL)
footer_part = footer_match.group(1)

# Clean up the script section in the footer to prevent errors due to missing chromeNav
footer_part = re.sub(r'function renderNav\(\).*?\}\s*renderNav\(\);', '', footer_part, flags=re.DOTALL)
# Also remove the initial highlight logic
footer_part = re.sub(r'// Highlight the initially-visible.*?\}\);', '', footer_part, flags=re.DOTALL)
# And the goTo function's dependency on surface-btn which is fine since querySelectorAll won't error, but we can leave it.

def build_file(surface_html, filename):
    # Set display:block on the surface
    surface_html = re.sub(r'style="display:\s*none;"', 'style="display:block;"', surface_html)
    
    full_html = head_part + '\n' + surface_html + '\n' + footer_part
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
        print(f"Created {filename}")

base_path = '/Users/guilhermerossi/Documents/AI_DW_Workflow'
build_file(surface_ad_match.group(1), os.path.join(base_path, 'index-ads.html'))
build_file(surface_act_match.group(1), os.path.join(base_path, 'index-dsa.html'))
build_file(surface_dw_match.group(1), os.path.join(base_path, 'index-drumwave.html'))
build_file(surface_idr_match.group(1), os.path.join(base_path, 'index-idr.html'))

