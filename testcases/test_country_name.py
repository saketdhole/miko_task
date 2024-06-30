import pytest

from resources.countryapi import CountryApi
from tools.common import Common


class Testcountryname:
    @pytest.fixture(params=Common().get_csv_data("Postivecountrytestcase.csv"))
    def country(self, request):
        return request.param

    @pytest.fixture(params=Common().get_csv_data("Negativecountrytestcase.csv"))
    def countryNegative(self, request):
        return request.param

    def test_get_country_name(self, country):
        countryapi = CountryApi()
        response = countryapi.get_country_by_name(country)
        countryapi.verify_json_content(response[0], ["name"])
        assert response[0]["name"]["common"] == country

    def test_get_country_name_negative(self, countryNegative):
        countryapi = CountryApi()
        response = countryapi.get_country_by_name(countryNegative,404)
        countryapi.verify_json_content(response, ["status"])
        assert response["message"] == "Not Found"
