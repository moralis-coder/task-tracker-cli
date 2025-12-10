from datetime import datetime

class InvalidTaskArgument(Exception):
    pass

class Task:
    @classmethod
    def from_dict(cls, data):
        task = cls(
            id=data.get('id'),
            title=data.get('title', ''),
            status=data.get('status', 'todo'),
            deleted=data.get('deleted', False),
        )
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.updated_at = datetime.fromisoformat(data['updated_at'])
        return task

    def __init__(self, id=None, title='', status='todo', deleted=False):
        time = datetime.now()
        self.id = id
        self.title = title
        self.status = status
        self.deleted = deleted
        self.created_at = time
        self.updated_at = time

    def delete(self):
        if self.deleted:
            raise InvalidTaskArgument(f'Task {self} is already deleted.')
        self.deleted = True
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

    def __str__(self):
        return f'{self.id}: {self.title} [{self.status}]'
