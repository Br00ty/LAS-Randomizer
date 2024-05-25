def makeDatasheetChanges(sheet, settings):
    """Iterates through all the values in the ItemDrop datasheet and makes changes"""
    
    for i in range(len(sheet['values'])):
        
        if sheet['values'][i]['mKey'] == 'HeartContainer0':
            first_heart_index = i
        
        if sheet['values'][i]['mKey'] == 'AnglerKey':
            sheet['values'][i]['mLotTable'][0]['mType'] = ''
        if sheet['values'][i]['mKey'] == 'FaceKey':
            sheet['values'][i]['mLotTable'][0]['mType'] = ''
        if sheet['values'][i]['mKey'] == 'HookShot':
            sheet['values'][i]['mLotTable'][0]['mType'] = ''
        
        if sheet['values'][i]['mKey'] == 'Bomb':
            if settings['reduce-farming']:
                sheet['values'][i]['mLotTable'][0]['mCookie'] = 3
        
        if sheet['values'][i]['mKey'] == 'MagicPowder':
            if settings['reduce-farming']:
                sheet['values'][i]['mLotTable'][0]['mCookie'] = 3
        
        if sheet['values'][i]['mKey'] == 'Arrow' and settings['reduce-farming']:
            sheet['values'][i]['mLotTable'][0]['mCookie'] = 3
        if sheet['values'][i]['mKey'] == 'Grass' and settings['reduce-farming']:
            sheet['values'][i]['mLotTable'][1]['mWeight'] = 18
            sheet['values'][i]['mLotTable'][2]['mWeight'] = 3
            sheet['values'][i]['mLotTable'][3]['mWeight'] = 71

    for i in range(8):
        sheet['values'][first_heart_index+i]['mLotTable'][0]['mType'] = ''
