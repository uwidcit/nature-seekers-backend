from App.models import Report
from App.database import db

import json

def create_report(userid):
    newreport = Report(userid=userid)
    db.session.add(newreport)
    db.session.commit()
    return newreport


def get_report(reportid):
    return Report.query.get(reportid)

def get_all_report_json():
    reports = Report.query.all()
    if not reports:
        return []
    return [report.toJSON() for report in reports]