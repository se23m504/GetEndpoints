import re


def is_valid_url(url):
    url_regex = re.compile(
        r"^(https?):\/\/"
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"
        r"(?::\d+)?"
        r"(?:\/[^\s]*)?$",
        re.IGNORECASE,
    )
    return re.match(url_regex, url) is not None
