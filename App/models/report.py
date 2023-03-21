from App.database import db

class Report(db.Model):
    reportId = db.Column(db.Integer, primary_key=True)
    userId  = db.Column(db.Integer, db.ForeignKey('user.id'))
    report = db.Column (db.String, nullable=False)

    def toJSON(self):
        return {
            'reportId': self.reportId,
            'userId': self.userId,
            'report': self.report
        }