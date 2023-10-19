from django import template
register = template.Library()

GENDER_CHOICES_URL = {
    'Dragonborn-M': 'images/dragonborn.png',
    'Dragonborn-F': 'images/dragonborn-female.jpeg',
    'Dwarf-M': 'images/Dwarf.webp',
    'Dwarf-F': 'images/dwarf-female.png',
    'Elf-M': 'images/elf-male.webp',
    'Elf-F': 'images/elf.png',
    'Gnome-M': 'images/gnome.webp',
    'Gnome-F': 'images/gnome-female.jpeg',
    'Half-elf-M': 'images/half-elf.jpeg',
    'Half-elf-F': 'images/half-elf.jpeg',
    'Half-orc-M': 'images/Half_Orc_male.webp',
    'Half-orc-F': 'images/half-orc-female.jpeg',
    'Halfling-M': 'images/halfling-male.png',
    'Halfling-F': 'images/halfling_female.jpeg',
    'Human-M': 'images/human_male.jpeg',
    'Human-F': 'images/human-female.png',
    'Tiefling-M': 'images/tiefling-male.jpeg',
    'Tiefling-F': 'images/tiefling-female.jpeg',
}

@register.filter
def gender_image_url(gender):
    return GENDER_CHOICES_URL.get(gender, 'URL_FOR_DEFAULT_IMAGE')
@register.filter
def lowercase_and_remove_hyphens(value):
    return value.lower().replace('-', '')

register.filter('gender_image_url', gender_image_url)
