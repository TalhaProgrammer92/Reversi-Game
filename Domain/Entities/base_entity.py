from uuid import uuid4, UUID
import datetime as dt

class BaseEntity:
    def __init__(self, **kwargs):
        self.id: UUID = kwargs.get("id", uuid4())
        self.created_at: dt.datetime = kwargs.get("created_at", dt.datetime.now())
        self.updated_at: dt.datetime | None = kwargs.get("updated_at", None)
