from App.models import Organization
from App.database import db

import json

def create_organization(userId, organizationId, description, email, phone, website):
    neworganization = Organization(userId=userId, organizationId=organizationId, description=description, email=email, phone=phone, website=website)
    db.session.add(neworganization)
    db.session.commit()
    return neworganization

def get_organization(organizationid):
    return Organization.query.get(organizationid)

def get_all_organization_json():
    organizations = Organization.query.all()
    if not organizations:
        return []
    return [organization.toJSON() for organization in organizations]


def delete_organization(id):
    organization = get_organization(id)
    if organization:
        db.session.delete(organization)
        return db.session.commit()
    return None