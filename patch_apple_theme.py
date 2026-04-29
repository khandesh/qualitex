import os

filepath = "css/styles-white.css"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Find the start of the white theme overrides
split_marker = "/* Premium white theme for index2.html. Original css/styles.css remains unchanged. */"
if split_marker in content:
    base_css = content.split(split_marker)[0]
else:
    print("Marker not found, please check")
    exit(1)

apple_theme_css = """/* Premium Apple-like white theme for index2.html. Original css/styles.css remains unchanged. */
:root {
  --ink: #1d1d1f;
  --ink-reverse: #ffffff;
  --muted: #86868b;
  --soft: rgba(255, 255, 255, 0.72);
  --soft-hover: rgba(255, 255, 255, 0.95);
  --surface: #f5f5f7;
  --surface-raised: #ffffff;
  --line: #d2d2d7;
  --line-strong: #c6c6c8;
  --blue: #0071e3;
  --blue-dark: #0077ed;
  --accent-grad: #0071e3;
  --accent-grad-hover: #0077ed;
  --silver: #f5f5f7;
  --green: #28cd41;
  --shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
  --glow: 0 8px 16px rgba(0, 113, 227, 0.2);
}

body {
  background: var(--surface);
  color: var(--ink);
}

body::before {
  display: none;
}

.topbar {
  background: #f5f5f7;
  color: #86868b;
  border-bottom: 1px solid var(--line);
}

.topbar-contact a {
  background: none;
  -webkit-text-fill-color: #1d1d1f;
  color: #1d1d1f;
}

.topbar-contact a:hover {
  color: #0071e3;
}

.navbar {
  background: rgba(251, 251, 253, 0.8);
  border-bottom-color: rgba(0, 0, 0, 0.08);
  box-shadow: none;
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
}

.brand {
  color: #1d1d1f;
  letter-spacing: -0.01em;
}

.brand-mark {
  background: #0071e3;
  border-radius: 10px;
  box-shadow: none;
}

.menu a {
  color: #1d1d1f;
  font-weight: 500;
}

.menu a:hover,
.menu a.active {
  color: #0071e3;
}

.menu a::after {
  background: #0071e3;
  height: 2px;
  bottom: -4px;
}

.menu-btn {
  color: #1d1d1f;
}

.hero {
  background: var(--surface);
  min-height: calc(100vh - 72px);
}

.hero-media {
  inset: 72px 0 0 auto;
  left: 50%;
  overflow: hidden;
  z-index: 0;
  border-radius: 30px 0 0 30px;
  box-shadow: -20px 0 60px rgba(0,0,0,0.06);
}

.hero-media::before, .hero-media::after {
  display: none;
}

.hero-media img {
  filter: none;
}

.hero-content {
  color: #1d1d1f;
  z-index: 5;
}

.hero h1 {
  color: #1d1d1f;
  letter-spacing: -0.02em;
  max-width: 760px;
}

.hero h1 span {
  background: none;
  -webkit-text-fill-color: #1d1d1f;
  color: #1d1d1f;
}

.lead,
.section-heading p,
.feature-layout p,
.certificate-panel p,
.page-intro p,
.split-copy p,
.service-card-rich p,
.service-detail-card p,
.check-list li,
.scope-list li,
td {
  color: #86868b;
  font-weight: 400;
}

.eyebrow {
  color: #86868b;
  letter-spacing: 0.1em;
  font-weight: 600;
}

.eyebrow::before {
  background: #86868b;
}

.btn {
  border-radius: 980px;
  box-shadow: none;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.btn-primary {
  background: #0071e3;
  color: #ffffff;
}

.btn-primary:hover {
  background: #0077ed;
  transform: scale(1.02);
  box-shadow: none;
}

.btn-plain,
.btn-muted,
.btn-light {
  background: #e8e8ed;
  border: none;
  color: #1d1d1f;
}

.btn-plain:hover,
.btn-muted:hover,
.btn-light:hover {
  background: #d2d2d7;
  border: none;
  transform: scale(1.02);
  box-shadow: none;
}

.metrics-strip {
  background: #ffffff;
  border-color: #d2d2d7;
  border-radius: 20px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
}

.metrics-strip div:hover {
  background: #fbfbfd;
}

.metrics-strip strong {
  background: none;
  -webkit-text-fill-color: #1d1d1f;
  color: #1d1d1f;
  font-size: clamp(1.5rem, 2.5vw, 2.2rem);
  font-weight: 700;
}

.metrics-strip span {
  color: #86868b;
  font-weight: 600;
}

.service-card,
.service-detail-card,
.panel,
.extract-card,
.scope-list {
  background: #ffffff;
  border-color: #d2d2d7;
  border-radius: 20px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.service-card::before {
  display: none;
}

.service-card:hover,
.service-detail-card:hover,
.extract-card:hover {
  background: #ffffff;
  border-color: #c6c6c8;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.08);
  transform: translateY(-4px) scale(1.01);
}

.service-card span, .service-detail-card span, .extract-card span {
  background: #0071e3;
  color: #fff;
  border: none;
  box-shadow: none;
}

.service-card span::after,
.service-detail-card span::after {
  display: none;
}

.feature-band,
.equipment-section,
.certificate-section {
  background: #f5f5f7;
  border-color: #d2d2d7;
  color: #1d1d1f;
}

.feature-band::before {
  display: none;
}

.media-frame,
.image-mosaic figure,
.gallery figure {
  background: #ffffff;
  border: 1px solid #d2d2d7;
  border-radius: 20px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
}

.media-frame img,
.image-mosaic img,
.gallery img {
  filter: none;
}

.slideshow {
  background: #f5f5f7;
}

.icon-btn {
  background: rgba(255, 255, 255, 0.8);
  border-color: #d2d2d7;
  color: #1d1d1f;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.icon-btn:hover,
.icon-btn.light:hover,
.icon-btn.light {
  background: #ffffff;
  border-color: #c6c6c8;
  color: #0071e3;
}

.certificate-panel {
  background: #ffffff;
  border-color: #d2d2d7;
  border-radius: 24px;
  box-shadow: 0 8px 36px rgba(0, 0, 0, 0.06);
  color: #1d1d1f;
}

.certificate-panel::after {
  display: none;
}

.footer {
  background: #f5f5f7;
  border-top-color: #d2d2d7;
  color: #86868b;
}

.footer h4,
.footer a,
td:first-child,
label,
.extract-card strong {
  color: #1d1d1f;
}

.footer a:hover,
.extract-card span {
  background: none;
  -webkit-text-fill-color: #0071e3;
  color: #0071e3;
}

.page-hero {
  background: #f5f5f7;
  border-bottom-color: #d2d2d7;
}

.table-wrap {
  background: #ffffff;
  border-color: #d2d2d7;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
}

th {
  background: #f5f5f7;
  color: #86868b;
}

tr:hover td {
  background: #fbfbfd;
}

input,
textarea {
  background: #ffffff;
  border: 1px solid #d2d2d7;
  color: #1d1d1f;
  border-radius: 12px;
}

input:focus,
textarea:focus {
  background: #ffffff;
  border-color: #0071e3;
  box-shadow: 0 0 0 4px rgba(0, 113, 227, 0.15);
}

code {
  background: #f5f5f7;
  color: #1d1d1f;
  border: 1px solid #d2d2d7;
}

@media (max-width: 720px) {
  .menu {
    background: rgba(251, 251, 253, 0.95);
    border-bottom-color: #d2d2d7;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
  }

  .hero-media {
    inset: 0;
    left: 0;
    border-radius: 0;
  }

  .hero-media::before, .hero-media::after {
    display: block;
    content: '';
    position: absolute;
  }
  
  .hero-media::after {
    inset: 0;
    background: linear-gradient(180deg, rgba(245, 245, 247, 0.3) 0%, rgba(245, 245, 247, 0.95) 58%, #f5f5f7 100%);
  }

  .hero,
  .hero-content {
    min-height: 680px;
  }

  .hero h1 {
    font-size: clamp(2.5rem, 12vw, 3.5rem);
  }
}
"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(base_css + apple_theme_css)

print("Styles updated successfully.")

