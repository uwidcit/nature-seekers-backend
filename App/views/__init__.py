from .user import user_views
from .nest import nest_views
# from .index import index_views
from .turtle import turtle_views
# from .media import media_views
# from .tagevent import tag_event_views
# from .turtletag import turtle_tag_views
from .excavation import excavation_views

# from .captures import captures_views
# from .orgEvent import orgEvent_views
# from .report import report_views
# from .sighting import sighting_views
# from .stranding import stranding_views
# from .organization import organization_views

# # new views should be add here

app_views = [
    
     user_views,
     nest_views,
#     index_views,
     turtle_views,
#     media_views,
#     tag_event_views,
#     turtle_tag_views,
     excavation_views,
#     captures_views,
#     orgEvent_views,
#     report_views,
#     sighting_views,
#     stranding_views,
#     organization_views
    
 ]