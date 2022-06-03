
import json
import clr
import System

clr.AddReference("System.Net")

from System.Net import WebClient, HttpRequestHeader

client = WebClient()

AIRTABLE_BASE_ID = "appX1ltGTSz0dt7dA"
AIRTABLE_TABLE_NAME = "revit-table"
AIRTABLE_API_KEY = "keyzPCqxCOmHI76Ew"
url = "https://api.airtable.com/v0/{}/{}/".format(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME)


def make_request(
        urgency, project, phase, name, consultant, request_type,
        request, assign, user_id, attachment, version
        ):
    data = {
        "records": [
            {
                "fields": {
                    "Urgency" : urgency,
                    "Project" : project,
                    "Phase" : phase,
                    "Name" : name,
                    "Consultant" : consultant,
                    "Request Type" : request_type,
                    "Request" : request,
                    "Assigned To" : assign,
                    "User_ID" : user_id,
                    "Version" : version,
                    "Attachment" : attachment
                }
            }
        ]
    }

    client.Headers[HttpRequestHeader.ContentType] = "application/json"
    client.Headers[HttpRequestHeader.Authorization] = "Bearer {}".format(AIRTABLE_API_KEY)
   
    client.UploadString(url, json.dumps(data))