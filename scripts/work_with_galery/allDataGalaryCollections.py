import csv
import logging
from random import randint
from time import sleep
from bs4 import BeautifulSoup

from url.getURL import GetURL
from work_with_galery.galaryGenComicsPages import GenComicsPages
from work_with_galery.galaryComicsInfo import GalaryComicsInfo
from work_with_galery.galaryPagesCount import GalaryPagesCount


class Data_Collector:

    def сrawler(self):

        del_part_link = 'https://readcomicsonline.ru/comic/'
        count = 1

        logging.basicConfig(filename='example.log',
                            encoding='utf-8', level=logging.DEBUG)
        # Pages cont----------------------------
        temp_data_count = GalaryPagesCount()

        gen_link = temp_data_count.get_pages_cont()

        # Generations all galary links----------
        temp_data = GenComicsPages()

        gen_link = temp_data.first_pass_links(
            int(gen_link[0]), int(gen_link[1]))

        # Work do not touch!--------------------------------------

        with open(f'data\data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['comicsNumberInPages', 'comicsID', 'comicsName',
                          'comicsLink', 'comicsCover']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for iter_galary_pages in range(len(gen_link)):

                sleep(randint(1, 3))
                # if iter_galary_pages == 2:
                #     break

                getURL = GetURL()

                temp_comicsName = GalaryComicsInfo()

                galary_html_document = getURL.getHTMLdocument(
                    gen_link[iter_galary_pages])

                temp_get_galary_comics = BeautifulSoup(
                    galary_html_document, 'html.parser')

                temp_count = (
                    len(temp_comicsName.galary_comics_info(temp_get_galary_comics)[3]))

                html_document = getURL.getHTMLdocument(
                    gen_link[iter_galary_pages])

                for temp_data_comics in range(temp_count):

                    soup = BeautifulSoup(html_document, 'html.parser')

                    # Get all comics names
                    logging.debug(temp_comicsName.galary_comics_info(
                        soup)[0][temp_data_comics])

                    writer.writerow(
                        {
                            'comicsNumberInPages': count,

                            'comicsID': temp_comicsName.galary_comics_info(
                                soup)[1][temp_data_comics].replace(
                                f'{del_part_link}', ''),

                            'comicsName': temp_comicsName.galary_comics_info(
                                soup)[0][temp_data_comics],

                            'comicsLink': temp_comicsName.galary_comics_info(
                                soup)[1][temp_data_comics],
                            'comicsCover': temp_comicsName.galary_comics_info(
                                    soup)[2][temp_data_comics],
                        })
                    count += 1
