from .user import user_views
from .nest import nest_views
from .nestOutcomes import nestOutcome_views
from .nestRelocation import nestRelocation_views
from .organizationEvent import organizationEvent_views
from .turtleEventMedia import turtleEventMedia_views
from .turtle import turtle_views
from .turtleEvent import turtleEvent_views
from .turtleActivity import turtleActivity_views
from .turtleBio import turtleBio_views
from .turtleInjury import turtleInjury_views
from .turtleTag import turtleTag_views
from .excavation import excavation_views
from .report import report_views
from .ar import ar_views
from .tag import tag_views
from .nestActivities import nestActivity_views

app_views = [
    
     user_views,
     nest_views,
     nestOutcome_views,
     nestRelocation_views,
     organizationEvent_views,
     turtle_views,
     turtleEvent_views,
     turtleEventMedia_views,
     turtleActivity_views,
     turtleBio_views,
     turtleInjury_views,
     turtleTag_views,
     excavation_views,
     report_views,
     ar_views,
     tag_views,
     nestActivity_views
 ]