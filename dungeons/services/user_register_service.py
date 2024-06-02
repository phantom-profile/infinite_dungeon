from dungeons.models import Adventurer
from lib.services_utils import BaseService


class UserRegisterService(BaseService):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def _execute(self):
        self.sanitize_name()
        if self.result.is_fail():
            return
        self.check_presence()
        if self.result.is_fail():
            return

        user = Adventurer.objects.create(name=self.name, uid=self.uid)
        return self._build_result(user=user)

    def check_presence(self):
        user: Adventurer = Adventurer.objects.filter(uid=self.uid).first()
        if user:
            self._add_error('presence', 'exists')
            self._add_error('name', user.name)

    def sanitize_name(self):
        try:
            self.name = self.name.split("/start ")[1].strip()
        except IndexError:
            return self._add_error('name', 'Enter your name with start command like "/start MyName"')

        if not self.name:
            self._add_error('name', 'Your name must contain characters and numbers')
