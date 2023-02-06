import re


class GetComicsPagination:

    def __init__(self):

        self.temp = []

    def build_pagination_links(self, arg):

        tag_ul = 'ul'

        tag_li = 'li'

        page_pagination = 'pagination'

        first_element_list = 1

        last_element_list = (-2)

        inner_ul = arg.find(f'{tag_ul}', class_=f'{page_pagination}')

        inner_items = [li.text.strip()
                       for li in inner_ul.find_all(f'{tag_li}')]

        for iteration in range(len(inner_items)):

            self.temp.append(inner_items[iteration])

        return [self.temp[first_element_list], self.temp[last_element_list]]
