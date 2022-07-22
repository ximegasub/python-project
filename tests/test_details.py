import os
import pytest
from datetime import datetime
from pkg_resources import resource_filename
from src.app import get_details, read_data, save_data, welcome

TEST_FILE_PATH = resource_filename(__name__, "test_data.json")
DETAILS = {'date': '2022-07-22', 'time': '14:37:15', 'timezone': 'America/La_Paz', 'hostname': 'dev-xime', 'ip_address': {'lo': ['127.0.0.1'], 'enp0s3': ['10.0.2.15'], 'docker0': ['172.17.0.1'], 'br-34c766108881': ['172.18.0.1'], 'veth0a9fd74': ['No IP addr'], 'veth637e850': ['No IP addr']}}

@pytest.fixture(autouse=True)
def clean_file():
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)

def test_get_details(mocker):
    ips = {"lo": ["127.0.0.1"],"enp0s3": ["10.0.2.15"],"docker0": ["172.17.0.1"],"br-34c766108881": ["172.18.0.1"], "veth0a9fd74": ["No IP addr"],"veth637e850": ["No IP addr"]}
    def save_data(details, path):
        pass
    mocker.patch("src.app.save_data", save_data)
    mocker.patch("src.app.read_data", read_data)
    mocker.patch("src.app.get_ips").return_value = ips
    mocker.patch("src.app.datetime").now.return_value = datetime(2022, 7, 22, 14, 37, 15)
    mocker.patch("src.app.tzlocal").get_localzone_name.return_value = "America/La_Paz"
    mocker.patch("src.app.socket").gethostname.return_value = "dev-xime"

    expected_value = get_details()
    assert expected_value == DETAILS


def test_welcome():
    assert welcome() == "Welcome to the docker final project"

def test_save_data(mocker):
    mocker.patch("src.app.read_data").return_value = {"details": []}
    data = save_data(DETAILS, TEST_FILE_PATH)
    expected_value = {}
    expected_value["details"] = []
    expected_value["details"].append(DETAILS)
    assert expected_value == data