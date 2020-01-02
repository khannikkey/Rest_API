import json
def is_json(data):
    try:
        p_data = json.loads(data) #To Convert in Python Dict
        # if Converted means Comming Data is Json only
        valid = True
    except ValueError:
        valid = False
    return valid
