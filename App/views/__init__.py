from .user import user_views
from .index import index_views
from .turtle import turtle_views
from .media import media_views

# new views should be add here

app_views = [
    user_views,
    index_views,
    turtle_views,
    media_views,
]