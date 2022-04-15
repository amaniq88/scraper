from cgi import test
from scraper.scraper import Webscraper
import pytest
import json
import re

def test_get_needed_count():
    web = Webscraper()
    actual = web.get_citations_needed_count()
    expected = 5
    assert actual == expected 
