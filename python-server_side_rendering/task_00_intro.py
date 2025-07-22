import os

"""
Function called: generate_invitations that takes tow parameters
    template: str
    attendees: list of dictionaries
"""

def generate_invitations(template, attendees):
    #  Check input types
    if not isinstance(template, str):
        print("Error: Template must be a str")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return
    
    if not all(isinstance(cont, dict) for cont in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for i, attendee in enumerate(attendees, start=1):
        output_file = f"output_{i}.txt"
        form_fillout = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A"),

        }
        try:
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(template.format(**form_fillout))
            print(f"Generated {output_file}")
        except KeyError as e:
            print(f"Error: Missing key {str(e)} in the template for attendee {i}")
