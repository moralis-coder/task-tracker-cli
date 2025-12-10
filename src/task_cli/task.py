from datetime import datetime

class Task:
    def __init__(self, id=None, title='', status='todo', deleted=False):
        self.id = id
        self.title = title
        self.status = status
        self.deleted = deleted
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __dict__(self):
        return {
            'id': self.id,
            'title': self.title,
            'status': self.status,
            'deleted': self.deleted,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
