from App.models import NestRelocation
from App.database import db

import json

#----------Create nestRelocation object
def create_nestRelocation(
                            nest_id, 
                            from_location_name, 
                            from_latitude, 
                            from_longitude, 
                            from_zone, 
                            from_distance_from_vege, 
                            from_distance_from_high_water, 
                            to_location_name, 
                            to_latitude, 
                            to_longitude, 
                            to_zone, 
                            to_distance_from_vege, 
                            to_distance_from_high_water
                          ):
    
    newnestRelocation = NestRelocation(
                                        nest_id=nest_id, 
                                        from_location_name=from_location_name, 
                                        from_latitude=from_latitude, 
                                        from_longitude=from_longitude, 
                                        from_zone=from_zone, 
                                        from_distance_from_vege=from_distance_from_vege, 
                                        from_distance_from_high_water=from_distance_from_high_water, 
                                        to_location_name=to_location_name, 
                                        to_latitude=to_latitude, 
                                        to_longitude=to_longitude, 
                                        to_zone=to_zone, 
                                        to_distance_from_vege=to_distance_from_vege, 
                                        to_distance_from_high_water=to_distance_from_high_water
                                    )
    db.session.add(newnestRelocation)
    db.session.commit()
    return newnestRelocation

#----------Get nestRelocation by nestRelocation_id
def get_nestRelocation(nestRelocation_id):
    return NestRelocation.query.get(nestRelocation_id)

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