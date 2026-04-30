import re

file_path = '/Users/guilhermerossi/Documents/AI_DW_Workflow/deploy_packages/site-dsa/data-savings.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update body
content = re.sub(
    r'body\s*\{\s*font-family:\s*\'Fraunces\',\s*serif;\s*background:\s*var\(--cream\);\s*color:\s*var\(--ink\);\s*font-size:\s*18px;\s*line-height:\s*1\.65;\s*font-weight:\s*400;\s*\}',
    r'''body {
  font-family: 'Inter', sans-serif;
  background: var(--cream);
  color: var(--ink);
  font-size: 16px;
  line-height: 1.5;
  font-weight: 400;
}''', content)

# 2. Update .hero h1
content = re.sub(
    r'\.hero h1\s*\{[^}]+\}',
    r'''.hero h1 {
  font-family: 'Fraunces', serif;
  font-size: 88px;
  font-weight: 400;
  line-height: 0.96;
  letter-spacing: -0.03em;
  margin: 0 auto 40px;
  max-width: 1000px;
}''', content)

# 3. Add mobile hero h1
content = re.sub(
    r'(\.hero-prose\s*\{)',
    r'''@media (max-width: 768px) {
  .hero h1 {
    font-size: 38px;
    line-height: 1.1;
  }
}
\1''', content)

# 4. Update .hero-form-title
content = re.sub(
    r'\.hero-form-title\s*\{[\s\S]*?\}',
    r'''.hero-form-title {
  font-family: 'Fraunces', serif;
  font-size: 48px;
  font-weight: 500;
  margin-bottom: 20px;
  color: #1a1a1a;
  letter-spacing: -0.01em;
  line-height: 1.1;
}''', content)

# 5. Update .section-head h2
content = re.sub(
    r'\.section-head h2\s*\{[^}]+\}',
    r'''.section-head h2 {
  font-family: 'Fraunces', serif;
  font-size: 42px;
  font-weight: 400;
  line-height: 1.08;
  letter-spacing: -0.02em;
  margin-top: 24px;
  max-width: 1000px;
}''', content)

# 6. .treaty-side h2
content = re.sub(
    r'\.treaty-side h2\s*\{[^}]+\}',
    r'''.treaty-side h2 {
  font-family: 'Fraunces', serif;
  font-size: 42px;
  font-weight: 400;
  line-height: 1.08;
  letter-spacing: -0.02em;
  margin-bottom: 50px;
}''', content)

# 7. .alternative h2
content = re.sub(
    r'\.alternative h2\s*\{[^}]+\}',
    r'''.alternative h2 {
  font-family: 'Fraunces', serif;
  font-size: 42px;
  font-weight: 400;
  line-height: 1.08;
  letter-spacing: -0.02em;
  margin-bottom: 80px;
  text-align: center;
}''', content)

# 8. .declaration h2
content = re.sub(
    r'\.declaration h2\s*\{[^}]+\}',
    r'''.declaration h2 {
  font-family: 'Fraunces', serif;
  font-size: 42px;
  font-weight: 400;
  line-height: 1.08;
  letter-spacing: -0.02em;
  margin: 0 auto 28px;
  text-wrap: balance;
  text-align: center;
  color: var(--ink);
}''', content)

# 9. .hero-prose p
content = re.sub(
    r'\.hero-prose p\s*\{[^}]+\}',
    r'''.hero-prose p {
  font-family: 'Fraunces', serif;
  font-size: 22px;
  font-weight: 400;
  line-height: 1.55;
  margin-bottom: 22px;
  color: #3a3430;
}''', content)

# 10. .transaction-content .lead
content = re.sub(
    r'\.transaction-content \.lead\s*\{[^}]+\}',
    r'''.transaction-content .lead {
  font-family: 'Fraunces', serif;
  font-size: 22px;
  font-weight: 400;
  line-height: 1.55;
  margin-bottom: 26px;
}''', content)

# 11. Add mobile queries for section headings and leads
content = re.sub(
    r'(@media \(max-width: 900px\) \{\s*\.transaction-content)',
    r'''@media (max-width: 768px) {
  .section-head h2, .treaty-side h2, .alternative h2, .declaration h2 {
    font-size: 32px;
  }
  .hero-prose p, .transaction-content .lead {
    font-size: 17px;
    line-height: 1.5;
  }
}
\1''', content)

# 12. Update generic paragraphs: .transaction-content p
content = re.sub(
    r'\.transaction-content p\s*\{[^}]+\}',
    r'''.transaction-content p {
  font-family: 'Fraunces', serif;
  font-size: 19px;
  line-height: 1.65;
  margin-bottom: 22px;
}''', content)

# 13. .backstop-content p
content = re.sub(
    r'\.backstop-content p\s*\{[^}]+\}',
    r'''.backstop-content p {
  font-family: 'Fraunces', serif;
  font-size: 19px;
  line-height: 1.65;
  margin-bottom: 22px;
}''', content)

# 14. .rhyme-content p
content = re.sub(
    r'\.rhyme-content p\s*\{[^}]+\}',
    r'''.rhyme-content p {
  font-family: 'Fraunces', serif;
  font-size: 19px;
  line-height: 1.65;
  margin-bottom: 22px;
}''', content)

# 15. .treaty-body p
content = re.sub(
    r'\.treaty-body p\s*\{[^}]+\}',
    r'''.treaty-body p {
  font-family: 'Fraunces', serif;
  font-size: 19px;
  line-height: 1.65;
  margin-bottom: 22px;
}''', content)

# 16. .alt-col p
content = re.sub(
    r'\.alt-col p\s*\{[^}]+\}',
    r'''.alt-col p {
  font-family: 'Fraunces', serif;
  font-size: 19px;
  line-height: 1.65;
  margin-bottom: 18px;
}''', content)

# 17. .funding-text-block p
content = re.sub(
    r'\.funding-text-block p\s*\{[^}]+\}',
    r'''.funding-text-block p {
  font-family: 'Fraunces', serif;
  font-size: 19px;
  line-height: 1.65;
  margin-bottom: 22px;
}''', content)

# 18. #signStep2Hero h2
content = re.sub(
    r'#signStep2Hero h2\s*\{[^}]+\}',
    r'''#signStep2Hero h2 {
  font-family: 'Fraunces', serif;
  font-size: 30px;
  font-weight: 500;
  margin: 0;
  color: #1a1a1a;
}''', content)

# 19. .hero .save-line
content = re.sub(
    r'\.hero \.save-line\s*\{[^}]+\}',
    r'''.hero .save-line {
  font-family: 'Fraunces', serif;
  font-weight: 600;
  font-size: 20px;
  font-style: italic;
  margin: 36px auto 0;
  color: var(--ink);
  text-wrap: balance;
  padding-top: 32px;
  border-top: 1px solid var(--line);
  max-width: 480px;
}''', content)

# 20. .form-field label
content = re.sub(
    r'\.form-field label\s*\{[^}]+\}',
    r'''.form-field label {
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 500;
  color: var(--ink-soft);
  margin-bottom: 10px;
}''', content)

# 21. .sign-form label
content = re.sub(
    r'\.sign-form label\s*\{[^}]+\}',
    r'''.sign-form label {
  display: block;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 500;
  color: #7a6e54;
  margin-bottom: 14px;
}''', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
