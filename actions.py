from typing import Any, Text, Dict, List
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType,SlotSet
from rasa_sdk.types import DomainDict
import os
import requests



def call_api(msg):
	
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a chatbot"},
                    {"role": "user", "content": msg},
                ]
        )
#0iliHLbAz3rgzdbA5h8rT3BlbkFJR2EbtjBqEelOs8Whp2zc
        result = ''
        for choice in response.choices:
            result += choice.message.content

        return(result)
class Actionapi(Action):

    def name(self) -> Text:
        return "action_call_openai"
    
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        context=tracker.latest_message['text']
        msg=call_api(context)
        dispatcher.utter_message(text=str(msg)) 
        return []
        
        



