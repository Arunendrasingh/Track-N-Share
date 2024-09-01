





# class Group(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True, nullable=False)
#     description = Column(String, index=True)
#     members = relationship("GroupMember", back_populates="group")
#     expenses = relationship("Expense", back_populates="group")

# class GroupMember(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     group_id = Column(Integer, ForeignKey('group.id'))
#     user = relationship("User", back_populates="groups")
#     group = relationship("Group", back_populates="members")

# class Notification(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     message = Column(String, index=True)
#     is_read = Column(Boolean, default=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship("User", back_populates="notifications")
