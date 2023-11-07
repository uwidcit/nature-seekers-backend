from App.models import NestRelocation
from App.database import db

import json

#----------Create nestRelocation object
def create_nestRelocation(
                            nest_id, 
                            to_location_name, 
                            to_latitude, 
                            to_longitude, 
                            to_zone,
                            to_timestamp 
                          ):
    
    newnestRelocation = NestRelocation(
                                        nest_id=nest_id, 
                                        to_location_name=to_location_name, 
                                        to_latitude=to_latitude, 
                                        to_longitude=to_longitude, 
                                        to_zone=to_zone,
                                        timestamp=to_timestamp
                                    )
    db.session.add(newnestRelocation)
    db.session.commit()
    return newnestRelocation

#----------Get nestRelocation by nestRelocation_id
def get_nestRelocation(nestRelocation_id):
    return NestRelocation.query.get(nestRelocation_id)

#----------Get turtle Relocation by nest_id
def get_turtleRelocation_by_nest_id(nest_id):
    turtleRelocations = NestRelocation.query.filter_by(nest_id=nest_id).all()
    return [turtleRelocation.toJSON() for turtleRelocation in turtleRelocations]


#----------Get all nestRelocations
def get_all_nestRelocation_json():
    nestRelocations = NestRelocation.query.all()
    if not nestRelocations:
        return []
    return [nestRelocation.toJSON() for nestRelocation in nestRelocations]

#----------Delete an nestRelocation by excavation_id
def delete_nestRelocation(nestRelocation_id):
    nestRelocation = get_nestRelocation(nestRelocation_id)
    if nestRelocation:
        db.session.delete(nestRelocation)
        return db.session.commit()
    return None