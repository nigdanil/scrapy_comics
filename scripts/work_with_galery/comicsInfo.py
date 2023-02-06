class ComicsInfo:

    def __init__(self):

        self.temp_name = []
        self.temp_links = []
        self.temp_cover_img = []

    def comics_info(self, soup):

        tag_a = 'a'

        tag_div = 'div'

        attribut_src = 'src'

        attribut_href = 'href'

        attribut_img = 'img'

        attribut_alt = 'alt'

        comics_cover = 'media-left'

        first_part_links = 'https:'

        temp_data = soup.find(f'{tag_div}', class_=f'{comics_cover}')

        inner_item_links = temp_data.find(f'{tag_a}', href=True)[
            f'{attribut_href}']

        inner_item_atributs = temp_data.findAll(f'{attribut_img}')

        for iteration in inner_item_atributs:

            self.temp_name.append(iteration[f'{attribut_alt}'])

            self.temp_cover_img.append(
                f'{first_part_links}'+iteration[f'{attribut_src}'])

            self.temp_links.append(inner_item_links)

        return self.temp_name, self.temp_links, self.temp_cover_img
