#!/usr/bin/env python
import logging
import sys

import ldclient

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

if __name__ == "__main__":
  ldclient.set_sdk_key("sdk-2b769201-47a8-40d2-9984-1cfbe3e537bb")

  user = {
    "key": "alice@example.com",
    "firstName": "Bob",
    "lastName": "Loblaw",
    "custom": {
      "groups": "beta_testers",
      "location": "NZ"
    }
  }

  show_feature = ldclient.get().variation("tali-hello-flag", user, False)

  if show_feature:
    print("Showing your feature")
  else:
    print("Not showing your feature")

  ldclient.get().close() # close the client before exiting the program - ensures that all events are delivered
