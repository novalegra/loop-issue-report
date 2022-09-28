import utils
import json
import os


def get_fixtures_from_report(name, report_extension):
    """ 
    Create Loop test fixtures from an issue report 

    path - path to file
    name - file name
    prefix - file prefix
    """
    path = utils.find_full_path(name, report_extension)
    report_name = name + report_extension

    parsed_report = utils.parse_report(path, report_name)

    utils.save_output(parsed_report, os.path.join(path, name + ".json"))


get_fixtures_from_report("meal_report1", ".md")
