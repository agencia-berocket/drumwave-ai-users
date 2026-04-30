#!/bin/bash
# Generate version-specific HTML files for social media crawlers on GitHub Pages

echo "Generating v1.html and v2.html for social sharing..."

cp index.html v1.html
sed -i '' 's|property="og:url" content="https://signtheact.datareserve.org"|property="og:url" content="https://signtheact.datareserve.org/v1.html"|g' v1.html

cp index.html v2.html
sed -i '' 's|property="og:url" content="https://signtheact.datareserve.org"|property="og:url" content="https://signtheact.datareserve.org/v2.html"|g' v2.html
sed -i '' 's|content="https://signtheact.datareserve.org/assets/img/share-option-1.jpg"|content="https://signtheact.datareserve.org/assets/img/share-option-2.jpg"|g' v2.html
sed -i '' 's/property="og:description" content="Machines Don.t Die. Own Your Data. Save Your Future."/property="og:description" content="The Data Savings Act. Your signature. Your voice. Public record."/g' v2.html
sed -i '' 's/name="twitter:description" content="Machines Don.t Die. Own Your Data. Save Your Future."/name="twitter:description" content="The Data Savings Act. Your signature. Your voice. Public record."/g' v2.html

echo "Done!"
