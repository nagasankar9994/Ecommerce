import json

import pytest

from NewProjects.conftest import browserInvoke
from PageObjectModel.LoginPage import LoginPage



ecommorce_test_data="C:\\Users\\nagas\\PycharmProject\\End2EndProjects\\test_ecommorece.json"

with open(ecommorce_test_data) as f:
    ecommorce_Data=json.load(f)
    ecommorce_list=ecommorce_Data["ecommorce_Data"]


@pytest.mark.parametrize("ecommorce_data",ecommorce_list)
def test_ecommorce(browserInvoke,ecommorce_data):
    driver=browserInvoke
    loginpage=LoginPage(driver)
    shoppage=loginpage.login(ecommorce_data["name_field"],ecommorce_data["email"])
    countrypage=shoppage.shop_item(ecommorce_data["mobile"])
    countrypage.country(ecommorce_data["expected_country"],ecommorce_data["actual_country"])