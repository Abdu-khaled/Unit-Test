
def CarSpeed(speed):
    
    if speed > 220 or speed < 0:
        return "Invalid"
    if speed < 40:
        return "Low"
    if speed < 120:
        return "Normal"
    if speed < 200:
        return "High"
    if speed <= 220:
        return "V.High"
    

# 0|--------40-----120-----------|220s