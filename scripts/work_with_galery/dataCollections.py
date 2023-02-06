import csv
from bs4 import BeautifulSoup

from url.getURL import GetURL
from work_with_galery.genComicsPages import GenComicsPages
from work_with_galery.getComicsPagination import GetComicsPagination
from work_with_galery.comicsInfo import ComicsInfo


class Data_Collector:

    def __init__(self):

        self.comics_pages_count = []

        self.comics_galary_pages = []

    def get_pages_cont(self):

        temp_gen_page = GenComicsPages()

        first_gen_page = temp_gen_page.first_pass_links(1, 1)

        for iteration in range(len(first_gen_page)):

            getURL = GetURL()

            html_document = getURL.getHTMLdocument(first_gen_page[iteration])

            soup = BeautifulSoup(html_document, 'html.parser')

            boo = GetComicsPagination()

            self.comics_pages_count = (boo.build_pagination_links(soup).copy())

        return self.comics_pages_count

    def gen_galary_pages(self):

        first_element_list = 0

        last_element_list = 1

        tem_data = self.get_pages_cont()

        temp_gen_page = GenComicsPages()

        self.comics_galary_pages = temp_gen_page.first_pass_links(
            int(tem_data[first_element_list]), int(tem_data[last_element_list])).copy()

        return self.comics_galary_pages

    def сrawler(self):

        tem_data = self.gen_galary_pages()

        temp_comicsName = ComicsInfo()

        temp_comicsLink = ComicsInfo()

        temp_comicsCover = ComicsInfo()

        with open(f'data\data.csv', 'w', newline='') as csvfile:
            fieldnames = ['comicsID', 'comicsName',
                          'comicsLink', 'comicsCover']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for first_iter in range(len(tem_data)):

                getURL = GetURL()

                html_document = getURL.getHTMLdocument(tem_data[first_iter])

                soup = BeautifulSoup(html_document, 'html.parser')

                comicsName = temp_comicsName.comics_info(soup)[0]
                comicsLink = temp_comicsLink.comics_info(soup)[1]
                comicsCover = temp_comicsCover.comics_info(soup)[2]

                if first_iter == 10:
                    break
                writer.writerow(
                    {'comicsID': first_iter,
                     'comicsName': comicsName[first_iter],
                     'comicsLink': comicsLink[first_iter],
                     'comicsCover': comicsCover[first_iter],
                     })
