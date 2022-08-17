import Tools.event_tools as event_tools
from Randomizers import item_get
from Randomizers import data



sunken = [
    'taltal-east-drop',
    'south-bay-sunken',
    'bay-passage-sunken',
    'river-crossing-cave',
    'kanalet-moat-south'
]



def changeHeartPiece(flowchart, item_key, item_index, model_path, model_name, room, room_data):
    """Applies changes to both the Heart Piece actor and the event flowchart"""

    hp = [a for a in room_data.actors if a.type == 0xB0]
    act = hp[0]
    
    if item_key != 'HeartPiece':
        if item_key[:3] == 'Rup': # no need for a fancy animation for rupees, just give them to the player
            itemGet = event_tools.createActionEvent(flowchart, 'Inventory', 'AddItemByKey',
            {'itemKey': item_key, 'count': 1, 'index': item_index, 'autoEquip': False})
        else:
            itemGet = item_get.insertItemGetAnimation(flowchart, item_key, item_index)
        
        event_tools.addEntryPoint(flowchart, room)
        event_tools.createActionChain(flowchart, room, [
            ('SinkingSword', 'Destroy', {}),
            ('EventFlags', 'SetFlag', {'symbol': data.HEART_FLAGS[room], 'value': True})
        ], itemGet)

        act.type = 0x194 # sinking sword

        if room in sunken:
            # if room not in ['taltal-east-drop', 'river-crossing-cave']:
            act.posY += 0.5 # move them up by 1/3 tile
        else:
            if room == 'mabe-well':
                act.posY += 0.5 # this heart piece always ends up barely visible, so raise by 1/3 tile
            else:
                act.posY += 0.25 # raise all others by 1/6 tile
        
        act.parameters[0] = bytes('ObjSinkingSword.bfres' if item_key == 'SwordLv1' else model_path, 'utf-8')
        act.parameters[1] = bytes('SinkingSword' if item_key == 'SwordLv1' else model_name, 'utf-8')
        act.parameters[2] = bytes(room, 'utf-8') # entry point
        act.parameters[3] = bytes(data.HEART_FLAGS[room], 'utf-8') # flag which controls if the heart piece appears or not
    else:
        act.parameters[0] = item_index # if item is a heart piece, just change the index in the parameter
