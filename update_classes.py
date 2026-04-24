import re

with open('testimonials1.html', 'r') as f:
    content = f.read()

replacements = {
    'testimonials-section': 'sd-testimonials-section',
    'container': 'sd-testimonials-container',
    'section-header': 'sd-section-header',
    'section-title': 'sd-section-title',
    'slider-controls': 'sd-slider-controls',
    'mySwiper': 'sd-mySwiper',
    't-card': 'sd-t-card',
    'stars': 'sd-stars',
    'star': 'sd-star',
    't-quote': 'sd-t-quote',
    't-author': 'sd-t-author',
    't-avatar': 'sd-t-avatar',
    't-name': 'sd-t-name',
    't-role': 'sd-t-role',
    'icon-star': 'sd-icon-star',
    'btn-prev': 'sd-btn-prev',
    'btn-next': 'sd-btn-next'
}

for old, new in replacements.items():
    # Replace class declarations in CSS
    content = re.sub(r'\.' + old + r'(?=[ \.\{:,])', '.' + new, content)
    # Replace class references in HTML (this regex is safe for our use case)
    content = re.sub(r'class="([^"]*?)' + old + r'([^"]*?)"', r'class="\1' + new + r'\2"', content)
    # IDs
    content = re.sub(r'id="' + old + '"', 'id="' + new + '"', content)
    content = re.sub(r'#' + old + r'(?=[ \.\{:,])', '#' + new, content)
    content = re.sub(r'href="#' + old + '"', 'href="#' + new + '"', content)

# Scope Swiper classes in CSS
swiper_classes = ['swiper-button-prev', 'swiper-button-next', 'swiper-wrapper', 'swiper-slide', 'swiper-slide-active']
for sc in swiper_classes:
    content = re.sub(r'\.' + sc + r'(?=[ \.\{:,])', '.sd-testimonials-section .' + sc, content)

with open('testimonials1.html', 'w') as f:
    f.write(content)

print("Done")
