from bs4 import BeautifulSoup

from url.getURL import GetURL
from work_with_galery.galaryGenComicsPages import GenComicsPages
from work_with_galery.galaryGetComicsPagination import GetComicsPagination


class GalaryPagesCount:

    def __init__(self):

        self.comics_pages_count = []

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
