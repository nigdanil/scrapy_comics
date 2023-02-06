from bs4 import BeautifulSoup

# from url.getURL import GetURL
from url.getURL import GetURL
from work_with_galery.genComicsPages import GenComicsPages
from work_with_galery.getComicsPagination import GetComicsPagination
from work_with_galery.comicsInfo import ComicsInfo
# from work_with_galery.aboutBook import AboutBook
# from work_with_galery.readPage import ReadPage
# from work_with_galery.regexBookPages import RegexBookPages
# from work_with_galery.loadDataLinks import LoadDataLinks as readDataLinks
# from work_with_galery.bookCover import BookCover


class Data_Collector:

    def __init__(self):

        self.comics_pages_count = []

        self.comics_galary_pages = []

        self.books_info_part_2 = []

        self.books_info_part_3 = []

        self.booksCovers = []

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

        print(len(tem_data))

        for i in range(len(tem_data)):
            # print(tem_data[i])

            getURL = GetURL()

            html_document = getURL.getHTMLdocument(tem_data[i])

            soup = BeautifulSoup(html_document, 'html.parser')

            boo = ComicsInfo()
            print(boo.comics_info(soup))


# fo = Data_Collector()

# fo.сrawler()
#     readData = readDataLinks()

#     links = readData.datad_books_links()

#     for i in range(len(links)):

#         getURL = GetURL()

#         html_document = getURL.getHTMLdocument(links[i])

#         soup = BeautifulSoup(html_document, 'html.parser')

#         # Create structure

#         dataComicsCover = ComicsCover()

#         prodInfo = BookInfo()

#         about = AboutBook()

#         readPage = ReadPage()

#         builder_links = RegexBookPages()

#         readPage = ReadPage()

#         # Pages links generator
#         self.book_pages.append(builder_links.build_book_links(
#             links[i], readPage.get_page_range(soup)))

#         self.booksCovers.append(dataBooksCover.book_cover(soup))

#         self.books_info_part_1.append(prodInfo.book_info(soup))

#         self.books_info_part_2.append(about.small_description(soup))

#         self.books_info_part_3.append(
#             readPage.get_page_range(soup)[-1])

# return self.books_info_part_1, self.books_info_part_2, self.books_info_part_3, self.book_pages, self.booksCovers
