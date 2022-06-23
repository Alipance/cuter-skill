from mycroft import MycroftSkill, intent_file_handler


class Cuter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cuter.intent')
    def handle_cuter(self, message):
        self.speak_dialog('cuter')


def create_skill():
    return Cuter()

