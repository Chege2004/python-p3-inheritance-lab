#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge = []):
        User.__init__(self, first_name, last_name)
        self.knowledge = knowledge
    def learn(self, new_knowledge):
        if isinstance(new_knowledge,str) and new_knowledge not in self.knowledge:
            return self.knowledge.append(new_knowledge)