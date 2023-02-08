class GenComicsPages:

    def __init__(self):

        self.temp = []

    def first_pass_links(self, firstElemet, lastElemet):

        first_part_str = 'https://readcomicsonline.ru/filterList?page='

        last_part_str = '&cat=&alpha=&sortBy=name&asc=true&author=&tag'

        for i in range(firstElemet, lastElemet + 1):

            self.temp.append(f'{first_part_str}{i}{last_part_str}')

        return self.temp
