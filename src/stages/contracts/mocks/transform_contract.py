# pylint: disable=line-too-long
import datetime
from src.stages.contracts.transform_contract import TransformContract

transform_contract_mock = TransformContract(
    load_content=[
        {'first_name': 'Giuseppe', 'second_name': 'Zanini', 'surname': None, 'artist_id': '11597', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597', 'extraction_date': datetime.date(2022, 4, 23)},
        {'first_name': 'Giuseppe', 'second_name': 'Zanini-Viola', 'surname': None, 'artist_id': '11597', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11597', 'extraction_date': datetime.date(2022, 4, 23)},
        {'first_name': 'Giampietro', 'second_name': 'Zanotti', 'surname': None, 'artist_id': '11631', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11631', 'extraction_date': datetime.date(2022, 4, 23)},
        {'first_name': 'Wou-Ki', 'second_name': 'Zao', 'surname': None, 'artist_id': '3427', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3427', 'extraction_date': datetime.date(2022, 4, 23)}
    ]
)
