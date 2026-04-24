import re

# Read original
with open('testimonials1.html', 'r') as f:
    content = f.read()

# Let's start fresh from testimonials.html (wait, let's just reset the file first or use a safer script on the original string, actually I don't have the original string saved). Let's just fix the double replacements.
content = content.replace('sd-sd-stars', 'sd-stars')
content = content.replace('sd-sd-star', 'sd-star')
content = content.replace('sd-sd-testimonials-section', 'sd-testimonials-section')

# Let's check Swiper JS initialization:
content = content.replace('.mySwiper', '.sd-mySwiper')
content = content.replace('#btn-next', '#sd-btn-next')
content = content.replace('#btn-prev', '#sd-btn-prev')

with open('testimonials1.html', 'w') as f:
    f.write(content)

print("Done")
