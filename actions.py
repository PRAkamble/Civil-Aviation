# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
import re

required_slots_list = ["email","mobile","age","license_type"]


class ActionCustomPayloadOne(Action):

    def name(self) -> Text:
        return "action_custom_payload"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        gt = {
            "type" : "Hyperlink",
            "level": "first_level",
            "title": "I am here to help you with the following services:",
            "links":[
                {
                    "payload":"Register to fly a drone or model aircraft",
                    "link_text": "Register for drones or model aircrafts"
                },
                {
                    "payload": "our roles",
                    "link_text": "Our roles"
                },
                {
                    "payload": "recreational unmanned aircraft",
                    "link_text": "Recreational unmanned aircraft"
                }
                ,
                {
                    "payload": "model aircraft",
                    "link_text": "Model aircraft"
                }
                 ,
                {
                    "payload": "commercial unmanned aircraft and drone operations",
                    "link_text": "Commercial unmanned aircraft and drone operations"
                }
                 ,
                {
                    "payload": "larger unmannned aircraft",
                    "link_text": "Larger unmannned aircraft"
                }
                 ,
                {
                    "payload": "information for public",
                    "link_text": "Information for public"
                }
                
            ]
        }
        print("Inside custom action payload")
        dispatcher.utter_custom_json(gt)

        return []


class ActionCustomPayloadTwo(Action):

    def name(self) -> Text:
        return "action_custom_payload_two"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        gt = {
            "type" : "Hyperlink",
            "level": "second_level",
            "title": "I am here to help you with the following sub services:",
            "links":[
                {
                    "payload":"Register yourself and take test",
                    "link_text": "Register yourself and take test",
                    "link_href": "https://register-drones.caa.co.uk/individual"
                },
                {
                    "payload": "Register a child under 13",
                    "link_text": "Register a child under 13",
                    "link_href": "https://register-drones.caa.co.uk/individual/register-an-under-13-child"
                },
                {
                    "payload": "Register an organization",
                    "link_text": "Register an organization",
                    "link_href": "https://register-drones.caa.co.uk/organisation/register"
                }
                ,
                {
                    "payload": "About Registration",
                    "link_text": "About Registration",
                    "link_href": "https://www.caa.co.uk/Consumers/Unmanned-aircraft/Our-role/Drone-and-model-aircraft-registration/"
                }
                 ,
                {
                    "payload": "The drone and model aircraft code",
                    "link_text": "The drone and model aircraft code",
                    "link_href": "https://register-drones.caa.co.uk/drone-code"
                }
                 ,
                {
                    "payload": "Labeling your drone and model aircraft",
                    "link_text": "Labeling your drone and model aircraft",
                    "link_href": "https://register-drones.caa.co.uk/labelling-your-drone-or-model-aircraft"
                }
            ]
        }
        print("Inside custom action payload")
        dispatcher.utter_custom_json(gt)

        return []




class ActionCustomPayloadThree(Action):

    def name(self) -> Text:
        return "action_custom_payload_three"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        gt = {
            "type" : "ImageSlider",
            "level": "second_level",
            "title": "Custom Image Slider",
            "Images":[
                {
                    "payload":"Register yourself and take test",
                    "img_text": "img1",
                    "img_src": "./static/img/carousel_images/1D7pKB3_1.jpg",
                    "class" : "img_slider"
                },
                {
                    "payload": "Register a child under 13",
                    "img_text": "img2",
                    "img_src": "./static/img/carousel_images/planet_green_space_151972_1024x768_2.jpg",
                    "class" : "img_slider"
                },
                
                {
                    "payload": "Register a child under 13",
                    "img_text": "img3",
                    "img_src": "./static/img/carousel_images/road_slope_turn_138884_1024x768_3.jpg",
                    "class" : "img_slider"
                },
                
                {
                    "payload": "Register a child under 13",
                    "img_text": "img4",
                    "img_src": "./static/img/carousel_images/road_trees_marking_121714_1024x768_4.jpg",
                    "class" : "img_slider"
                }
            ]
        }
        print("Inside custom action payload")
        dispatcher.utter_custom_json(gt)

        return []


        
class ActionResetSlot(Action):

    def name(self) -> [Text]:
        return "action_reset_slot_values"

    def run(self, dispatcher : CollectingDispatcher,
            tracker : Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global required_slot_list
        required_slot_list = ["email","mobile","age","license_type"]

        return []    

class LicenseRegisterForm(FormAction):
    
    def name(self):
        return "license_register_form"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print("Inside required slot")
        return required_slots_list


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        print("slot mapping")
        
        return{
   			"email":[self.from_text()],
            "mobile":[self.from_text()],
            "age":[self.from_text()],
            "license_type":[self.from_text()]
		}

    def validate_email(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[Text]:
        email = re.search(r'[\w\.-]+@[\w\.-]+', value) 
        if (email):
            return {"email" : value}
        else:
            dispatcher.utter_message("Please re-enter valid email Id")
            return {"email" : None}


    def validate_mobile(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[Text]:
        mobile = re.search(r'[0-9]{10}', value)
        if (mobile):
            return {"mobile" : value}
        else:
            dispatcher.utter_message("Please enter 10 digit mobile number")
            return {"mobile" : None}




    def validate_age(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[Text]:
            return {"age" : value}
        

         

    def validate_license_type(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[Text]:
        return {"license_type" : value}

        # response = requests.post('http://10.0.0.25:8088/MINDS_CONNECT/loginCheck?person_name={}&person_email_id={}&person_mobile_number{}&provide_comment{}'.format(tracker.get_slot('person_name'),('person_email_id'),('person_mobile_number'),('provide_comment')value))
        
        # if response.json() != None:
        #     self.write("Data saved successfullly")
        #     self.set_status(200)
        # else:
        #     self.write("Unable to save data")
        #     self.set_status(401)} 
        
    
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker,domain: Dict[Text, Any]):
        print("Inside submit")

        dispatcher.utter_template('utter_submit',tracker) 

        return []

    



