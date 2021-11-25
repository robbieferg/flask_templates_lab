from models.event import *

event_1 = Event("25/05/2031", "CodeClan Reunion", 18, "The G28 Hall", "A reunion for the G28 class of 2021/2022", True)
event_2 = Event("06/06/2032", "Annual Bakers Conference", 26, "The Green Kitched", "The world's foremost bakers get together for chat.", False)

events = [event_1, event_2]

def add_event(event):
    events.append(event)