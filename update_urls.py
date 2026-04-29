import os

domain = "https://qualitexsambhajinagar.in"
old_domain_1 = "https://www.qualitex.in"
old_domain_2 = "https://qualitex.example.com"

files_to_update = [
    "index.html",
    "about.html",
    "services.html",
    "accreditation.html",
    "contact.html",
    "sitemap.xml",
    "robots.txt"
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content.replace(old_domain_1, domain).replace(old_domain_2, domain)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
