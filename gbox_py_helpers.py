from pathlib import Path
from mailjet_rest import Client
import pickle
import os
from os import path, environ

# Function that leverages MailJet to send a bug report email to the user and developer

def bug_report(from_gbox, developer="lana.garmire.group@gmail.com", error_message=""):

    # Takes the stack traceback as an argument to email
    with open(path.join(environ.get("GRANATUM_SWD", ""), "shared.pkl"), "rb") as fp:
        shared = pickle.load(fp)
        email_address = shared["email_address"]

    api_key = os.environ['API_KEY']
    api_secret = os.environ['API_SECRET']

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": "lana.garmire.group@gmail.com",
            "Name": "GranatumX pipeline"
          },
          "To": [
            {
              "Email": developer,
              "Name": "Developer"
            },
            {
              "Email": email_address,
              "Name": "User"
            }
          ],
          "Subject": "Bug report in " + from_gbox,
          "TextPart": "There was an error encountered in the " + from_gbox + " step of the GranatumX pipeline: \n\n" + error_message
        }
      ]
    }
    result = mailjet.send.create(data=data)
