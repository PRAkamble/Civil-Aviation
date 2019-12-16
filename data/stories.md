## Intial greeting
* greet
  - utter_main_services

## Drones department1
* drones_dept
  - action_custom_payload

## Drones department2
* greet
  - utter_main_services
* drones_dept
  - action_custom_payload

## Drones department3
* greet
  - utter_main_services
* drones_dept
  - action_custom_payload
* register_drones_dept
  - action_custom_payload_two
* register_yourself
  - utter_show_license_types
* register_for_license{"license_type":"Flyer ID"}
  - license_register_form
  - form{"name":"license_register_form"}
  - form{"name": null}
  - utter_test_link

## Drones department4
* register_for_license{"license_type":"Flyer ID"}
  - license_register_form
  - form{"name":"license_register_form"}
  - form{"name": null}
  - utter_test_link


## thanks giving story
* thanks
  - utter_thanks

## Drones department5
* greet
  - utter_main_services
* drones_dept
  - action_custom_payload
* register_drones_dept
  - action_custom_payload_two
* register_yourself
  - utter_show_license_types
* register_for_license{"license_type":"Flyer ID"}
  - license_register_form
  - form{"name":"license_register_form"}
  - form{"name": null}
  - utter_test_link
* thanks
  - utter_thanks


## Q&A about drone suspecious activity
* drone_suspecious_activity
  - utter_on_drone_suspecious_activity

## Q&A about difference between drone and model aircraft
* diff_model_drone_aircraft
  - utter_diff_btwn_drone_model_aircraft

## Q&A about drone
* drone
  - utter_about_drone

## Q&A about model aircraft
* model_aircraft
  - utter_about_model_aircraft


## Q&A flow one
* drone_suspecious_activity
  - utter_on_drone_suspecious_activity
* diff_model_drone_aircraft
  - utter_diff_btwn_drone_model_aircraft
* drone
  - utter_about_drone
* model_aircraft
  - utter_about_model_aircraft