import os

"""
Function called: generate_invitations that takes tow parameters
    template: str
    attendees: list of dictionaries
"""

def generate_invitations(template, attendees):
    #  Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")

