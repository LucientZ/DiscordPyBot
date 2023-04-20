import os, json, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adds parent directory to PATH
import datahandling, helper
from test_utils import *


def test_user_profile_init() -> None:
     user1 = datahandling.UserProfile(string_user_ids[0])
     user2 = datahandling.UserProfile(string_user_ids[1])

     assert(user1 != user2)
     assert(user1.get_id() != user2)
     assert(user1.get_username() == "")
     assert(user2.get_username() == "")


     clean()