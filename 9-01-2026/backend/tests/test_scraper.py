from services.scraper import scrape

def test_scrape_valid_url():
    url = "https://www.coursera.org"
    data = scrape(url)

    assert isinstance(data, list)
    assert len(data) > 0

def test_scrape_invalid_url():
    try:
        scrape("invalid_url")
        assert False
    except:
        assert True
