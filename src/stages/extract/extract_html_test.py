from src.drivers.tests.http_requester import HttpRequesterSpy
from src.drivers.tests.html_collector import HtmlCollectorSpy
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError
from .extract_html import ExtractHtml

def test_extract():
    http_requeser_spy = HttpRequesterSpy()
    html_collector_spy = HtmlCollectorSpy()

    extract_html = ExtractHtml(http_requeser_spy, html_collector_spy)
    response = extract_html.extract()

    assert http_requeser_spy.count == 1
    assert 'html' in html_collector_spy.collect_essential_information_attributes

    assert isinstance(response, ExtractContract)


def test_extract_error():
    html_collector_spy = HtmlCollectorSpy()

    extract_html = ExtractHtml('Erro Aqui', html_collector_spy)

    try:
        extract_html.extract()
    except Exception as exception: # pylint: disable=broad-except
        assert isinstance(exception, ExtractError)
