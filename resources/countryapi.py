from urllib.parse import urljoin
from resources.componentbase import ComponentBase


class CountryApi(ComponentBase):
    COUNTRY_NAME_PATH = "v3.1/name/{0}"

    def get_country_by_name(self, countryname,checkcode=200):
        countrypath = self.COUNTRY_NAME_PATH.format(countryname)
        url = urljoin(self.baseurl, countrypath)
        response = self.assert_request("GET", url=url,codecheck=checkcode)
        return response.json()


