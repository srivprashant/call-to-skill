from mycroft import MycroftSkill, intent_file_handler


class CallTo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('to.call.intent')
    def handle_to_call(self, message):
        person = self.get_response('call.who')
        self.speak_dialog('to.call', {'person': person})


def create_skill():
    return CallTo()

