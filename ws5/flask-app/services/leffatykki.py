import requests
import xml.etree.ElementTree as ET

class LeffaTykkiRSS(object):
    movie_reviews_url = "http://www.leffatykki.com/xml/rss/leffat"

    def get_movie_reviews(self):
        r = requests.get(self.movie_reviews_url)
        root = ET.fromstring(r.content)
        items = root.findall('channel/item')
        return self._parse_reviews(items)

    def _parse_reviews(self, reviews):
        review_container = {}
        for review in reviews:
            title = review.find('title').text
            link = review.find('link').text
            review_container[title] = link
        return review_container
