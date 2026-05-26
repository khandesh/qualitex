import os

SEO_BASE_KEYWORDS = (
    "concrete testing lab Sambhajinagar, material testing laboratory Aurangabad, "
    "NABL accredited lab Aurangabad, civil engineering lab Sambhajinagar, "
    "soil testing Aurangabad, NDT testing Sambhajinagar, pile integrity test Aurangabad, "
    "concrete mix design Sambhajinagar, structural audit Aurangabad, "
    "construction quality testing, qualitex test house, Chikalthana lab"
)

PAGES = {
    "index.html": {
        "title": "Qualitex Test House | NABL Concrete & Material Testing Lab in Sambhajinagar (Aurangabad)",
        "desc": "Qualitex Test House is a premium NABL accredited civil engineering and construction material testing laboratory in Chhatrapati Sambhajinagar (Aurangabad). Expert soil testing, concrete mix design, NDT, and structural audit services.",
        "canonical": "https://qualitexsambhajinagar.in/"
    },
    "about.html": {
        "title": "About Qualitex | NABL Accredited Concrete & Material Testing Lab",
        "desc": "Learn about Qualitex Test House, a leading NABL accredited civil engineering testing lab in Chhatrapati Sambhajinagar (Aurangabad). Our quality commitment, team, and infrastructure.",
        "canonical": "https://qualitexsambhajinagar.in/about.html"
    },
    "services.html": {
        "title": "Testing Services | Concrete, Soil & NDT Testing | Qualitex Sambhajinagar",
        "desc": "Comprehensive construction material testing services at Qualitex Sambhajinagar (Aurangabad). We offer concrete cube testing, soil investigation, pile integrity tests, and advanced NDT.",
        "canonical": "https://qualitexsambhajinagar.in/services.html"
    },
    "accreditation.html": {
        "title": "NABL Accreditation & ISO 17025 | Qualitex Test House",
        "desc": "Qualitex Test House is an ISO/IEC 17025:2017 certified and NABL accredited testing laboratory (Certificate TC-16872) for civil engineering materials and geotechnical investigation in Sambhajinagar.",
        "canonical": "https://qualitexsambhajinagar.in/accreditation.html"
    },
    "contact.html": {
        "title": "Contact Qualitex | Material Testing Lab in Sambhajinagar (Aurangabad)",
        "desc": "Get in touch with Qualitex Test House in Chikalthana, Chhatrapati Sambhajinagar (Aurangabad) for reliable concrete testing, NDT, pile testing, and geotechnical soil investigation.",
        "canonical": "https://qualitexsambhajinagar.in/contact.html"
    }
}

JSON_LD = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Qualitex Test House Chhatrapati Sambhajinagar Pvt. Ltd.",
    "image": "https://qualitexsambhajinagar.in/images/equipments1.webp",
    "@id": "https://qualitexsambhajinagar.in/#localbusiness",
    "url": "https://qualitexsambhajinagar.in",
    "telephone": "+918956699841",
    "priceRange": "$$",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Gut No. 162, Plot No. N-9, Chikalthana",
      "addressLocality": "Chhatrapati Sambhajinagar",
      "addressRegion": "Maharashtra",
      "postalCode": "431006",
      "addressCountry": "IN"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 19.8732,
      "longitude": 75.4054
    },
    "hasMap": "https://maps.app.goo.gl/khom6VyCfSY3riBWA",
    "openingHoursSpecification": {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
      ],
      "opens": "09:00",
      "closes": "18:00"
    },
    "sameAs": [
      "https://maps.app.goo.gl/khom6VyCfSY3riBWA"
    ],
    "areaServed": [
      {
        "@type": "AdministrativeArea",
        "name": "Chhatrapati Sambhajinagar"
      },
      {
        "@type": "AdministrativeArea",
        "name": "Aurangabad"
      },
      {
        "@type": "AdministrativeArea",
        "name": "Maharashtra"
      }
    ],
    "description": "NABL accredited testing laboratory in Chhatrapati Sambhajinagar (Aurangabad) specializing in concrete testing, geotechnical soil investigation, NDT, pile testing, and construction material analysis."
  }
  </script>"""

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <head> and the preconnect link
    head_start = content.find("<head>")
    preconnect_start = content.find('<link rel="preconnect"')
    
    if head_start != -1 and preconnect_start != -1:
        page_info = PAGES.get(filename)
        title = page_info["title"]
        desc = page_info["desc"]
        canonical = page_info["canonical"]
        
        # Build the new head block
        new_head = f"""<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{SEO_BASE_KEYWORDS}" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <title>{title}</title>
{JSON_LD}
  """
        # Reconstruct content
        new_content = content[:head_start] + new_head + content[preconnect_start:]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Skipped {filename} (could not find head or preconnect tags)")

for page in PAGES.keys():
    if os.path.exists(page):
        update_file(page)
