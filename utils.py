from loop.issue_report import parser
import json
import os


from datetime import datetime
from pathlib import Path


def issue_report_date_parser(date_string):
    return datetime.strptime(date_string.strip(), "%Y-%m-%d %H:%M:%S %z").strftime(
        "%Y-%m-%dT%H:%M:%S"
    )


def save_output(output, output_path):
    with open(output_path, "w") as p:
        json.dump(output, p, indent=2)


def parse_report(path, file_name):
    try:
        lr = parser.LoopReport()
        parsed_issue_report_dict = lr.parse_by_file(path, file_name)
    except:
        raise RuntimeError("Unable to parse report")

    return parsed_issue_report_dict


def find_full_path(resource_name, extension):
    """ Find file path, given name and extension
        example: "/home/pi/Media/tidepool_demo.json"

        This will return the *first* instance of the file

    Arguments:
    resource_name -- name of file without the extension
    extension -- ending of file (ex: ".json")

    Output:
    path to file
    """
    search_dir = Path(__file__).parent.parent
    for root, dirs, files in os.walk(search_dir):
        for name in files:
            (base, ext) = os.path.splitext(name)
            if base == resource_name and extension == ext:
                return root

    raise Exception("No file found for specified resource name & extension")
