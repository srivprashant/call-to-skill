from mycroft import MycroftSkill, intent_file_handler


class CallTo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('to.call.intent')
    def handle_to_call(self, message):
        self.speak_dialog('to.call')


def create_skill():
    return CallTo()

