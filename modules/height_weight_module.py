#Retrieves height data and transfers it from metric to imperial
def get_height(dict):
    cm = dict.toInt()*10
    raw_height = str(cm/30.48).split(".")
    feet = raw_height[0]
    inches = float(".0" + raw_height[1]) * 12
    inches = str(float(round(inches,1))).replace('.','')
    full_height = f"{feet}' {inches}''"
    return full_height

#Retrieves weight data and transfers it from metric to imperial
def get_weight(dict):
    weight = float(dict.toInt()/10) * 2.20462262
    final_weight = str(round(weight,1))
    return final_weight