class GalaryComicsInfo:

    def __init__(self):

        self.temp_name = []
        self.temp_links = []
        self.temp_cover_img = []

    def galary_comics_info(self, soup):

        tag_div = 'div'

        attribut_src = 'src'

        attribut_href = 'href'

        attribut_alt = 'alt'

        class_tag = 'class'

        comics_class = 'media-left'

        first_part_links = 'https:'

        self.results = soup.find_all(
            f'{tag_div}', attrs={f'{class_tag}': f'{comics_class}'})

        for div in self.results:

            self.temp_name.append(div.img[f'{attribut_alt}'])

            self.temp_links.append(div.a[f'{attribut_href}'])

            self.temp_cover_img.append(
                f'{first_part_links}' + div.img[f'{attribut_src}'])

        return self.temp_name, self.temp_links, self.temp_cover_img, self.results
