from sqlalchemy import Boolean, Column, Integer, String, Date

from db import Base


class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    content = Column(String(200))
    created_at = Column(Date)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at} 