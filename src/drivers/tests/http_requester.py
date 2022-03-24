class HttpRequesterSpy:

    def __init__(self) -> None:
        self.count = 0

    def request_from_page(self):
        self.count += 1
        return { "status_code": 200, "html": "<h1>OlaMundo</h1>" }
