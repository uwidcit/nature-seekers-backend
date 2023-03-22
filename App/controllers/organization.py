from App.models import Organization
from App.database import db

import json

def create_organization(description, email, phone, website):
    neworganization = Organization(description=description, email=email, phone=phone, website=website)
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

#Update organization data 
def edit_organization_data(organization_id, new_description, new_email, new_phone, new_website):
    organization = Organization.query.filter_by(orgid=organization_id).first()
    if not organization:
        return ["organization not found"]

    if(new_description != "na"):
        organization.description = new_description
    if(new_email != "na"):
        organization.email = new_email
    if(new_phone != "na"):
        organization.phone = new_phone
    if(new_website != "na"):
        organization.website = new_website

    db.session.add(organization)
    db.session.commit()

    return [organization.toJSON()]

def delete_organization(id):
    organization = get_organization(id)
    if organization:
        db.session.delete(organization)
        return db.session.commit()
    return None