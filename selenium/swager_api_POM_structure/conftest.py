import pytest
from api.pet_api import PetAPI

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture(scope="session")
def pet_api():
    return PetAPI()