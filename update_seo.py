import os
import re

SEO_BASE_KEYWORDS = "lab, concrete testing, qualitex, lab house, soil testing, NDT, material testing, civil engineering laboratory, NABL accredited, Sambhajinagar, construction quality, building testing"

PAGES = {
    "index.html": {
        "title": "Qualitex Test House | NABL Accredited Concrete & Material Testing Lab in Sambhajinagar",
        "desc": "Qualitex Test House is a premium NABL accredited civil engineering and concrete testing laboratory in Sambhajinagar. We provide expert testing for soil, concrete, NDT, and construction materials.",
    },
    "about.html": {
        "title": "About Qualitex | NABL Accredited Concrete & Material Testing Lab House",
        "desc": "Learn about Qualitex Test House, a leading NABL accredited concrete testing lab in Sambhajinagar. Discover our commitment to quality, accuracy, and infrastructure.",
    },
    "services.html": {
        "title": "Testing Services | Concrete, Soil & NDT Testing | Qualitex Lab House",
        "desc": "Explore comprehensive material testing services at Qualitex Lab House. We offer concrete testing, soil testing, Non-Destructive Testing (NDT), and site sample collection.",
    },
    "accreditation.html": {
        "title": "NABL Accreditation | Qualitex Test House | Quality Concrete Testing Lab",
        "desc": "Qualitex Test House is an ISO/IEC 17025:2017 certified and NABL accredited laboratory for civil engineering and material testing. View our credentials.",
    },
    "contact.html": {
        "title": "Contact Qualitex | Concrete Testing Lab & Material Testing House",
        "desc": "Get in touch with Qualitex Test House for reliable concrete testing, NDT, and material testing services. Schedule a site visit or request a consultation.",
    }
}

JSON_LD = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Qualitex Test House Chhatrapati Sambhajinagar Pvt. Ltd.",
    "image": "https://qualitex.example.com/images/equipments1.webp",
    "url": "https://qualitex.example.com",
    "telephone": "+919657126633",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Gut No. 162, Plot No. N-9, Chikalthana",
      "addressLocality": "Chhatrapati Sambhajinagar",
      "addressRegion": "Maharashtra",
      "addressCountry": "IN"
    },
    "description": "NABL accredited testing laboratory in Sambhajinagar specializing in concrete testing, soil testing, and NDT."
  }
  </script>
"""

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    page_info = PAGES.get(filename, PAGES["index.html"])
    title = page_info["title"]
    desc = page_info["desc"]
    
    # Regex to find everything between <head> and <link rel="preconnect"
    pattern = re.compile(r'(<head>\s*<meta charset="UTF-8" />\s*<meta name="viewport" content="[^"]+" />\s*<meta name="description" content="[^"]*" />\s*<title>[\s\S]*?</title>\s*)(<link rel="preconnect")', re.IGNORECASE | re.MULTILINE)
    
    replacement = f"""<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{SEO_BASE_KEYWORDS}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <title>{title}</title>
{JSON_LD}
  \\2"""

    new_content = pattern.sub(replacement, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {filename}")

for page in PAGES.keys():
    if os.path.exists(page):
        update_file(page)

