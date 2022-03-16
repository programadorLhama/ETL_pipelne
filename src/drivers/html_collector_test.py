from .html_collector import HtmlCollector
from .mocks.http_requester_mock import mock_request_from_page


def test_collect_essential_information():
    http_request_response = mock_request_from_page()

    html_collector = HtmlCollector()
    essential_information = html_collector.collect_essential_information(http_request_response["html"])

    assert isinstance(essential_information, list)
    assert isinstance(essential_information[0], dict)
    assert 'name' in essential_information[0]
    assert 'link' in essential_information[0]
