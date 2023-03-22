from App.database import db
from datetime import *
import enum


class Outcome(enum.Enum):
    BODY_PIT_OLNY_OUTCOME_UNKNOWN = "body_pit_only_outcome_unknown"
    CONFIRMED_FALSE_CRAWL_WITH_BODY_PIT = "confirmed_false_crawl_with_body_pit"
    CONFIRMED_LAY = "confirmed_lay"
    ESTIMATED_LAY = "estimated_lay"
    FALSE_CRAWL_WITHOUT_BODY_PIT = "false_crawl_without_body_pit"
    UNKNOWN_OUTCOME = "unknown_outcome"

class NestOutcome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nest_id = db.Column(db.Integer, db.ForeignKey('nest.id'))
    outcome = db.Column(db.Enum(Outcome))
    timestamp =  db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def toJSON(self):
        return {
            'id': self.id,
            'nest_id': self.nest_id,
            'outcome': self.outcome.name,
            'timestamp': self.timestamp.strftime("%Y/%m/%d, %H:%M:%S")
        }