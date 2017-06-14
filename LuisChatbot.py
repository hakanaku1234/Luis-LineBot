from luis_wrapper import LuisWrapper
from utils.env_setting import get_env_variable
from task_modules.task_switch import TaskSwitcher

LUIS_APPID = get_env_variable('APPID')
LUIS_APPKEY = get_env_variable('APPKEY')

class Chatbot(object):

    '''
    A Chatbot using LUIS for NLU part.
    '''

    def __init__(self):

        self.task_switcher = TaskSwitcher()
        self.luis_wrapper = LuisWrapper(LUIS_APPID, LUIS_APPKEY)

    def get_response(self, query):

        top_intent, entities = self.luis_wrapper.predict(query)
        handler = self.task_switcher.get_task_handler(top_intent)
        response = handler.get_response(entities)

        return response

def main():

    c = Chatbot()
    print(c.get_response('通識演講'))
    print(c.get_response('我想吃甜點'))

if __name__ == "__main__":
    main()