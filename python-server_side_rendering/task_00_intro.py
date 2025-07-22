import os

"""
Function called: generate_invitations that takes two parameters
    template: str
    attendees: list of dictionaries
"""

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files for each attendee using a template.

    Args:
        template (str): The invitation template string with placeholders.
        attendees (list): List of dictionaries, each containing attendee and event info.

    Each output file is named 'output_{i}.txt' where i is the attendee number.
    """
    #  Check input types
    if not isinstance(template, str):
        # Ensure the template is a string
        print("Error: Template must be a str")
        return
    
    if not isinstance(attendees, list):
        # Ensure attendees is a list
        print("Error: Attendees must be a list of dictionaries")
        return
    
    if not all(isinstance(cont, dict) for cont in attendees):
        # Ensure every attendee is a dictionary
        print("Error: Attendees must be a list of dictionaries")
        return

    if not template.strip():
        # Handle empty template
        print("Template is empty, no output files generated")
        return
    
    if not attendees:
        # Handle empty attendee list
        print("No data provided, no output files generated.")
        return

    # Generate an output file for each attendee
    for i, attendee in enumerate(attendees, start=1):
        output_file = f"output_{i}.txt"
        # Prepare data for template filling, using 'N/A' for missing fields
        form_fillout = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A"),
        }
        try:
            # Write the filled template to the output file
            with open(output_file, 'w', encoding='utf-8') as output:
                output.write(template.format(**form_fillout))
            print(f"Generated {output_file}")
        except KeyError as e:
            # Handle missing keys in the template
            print(f"Error: Missing key {str(e)} in the template for attendee {i}")
