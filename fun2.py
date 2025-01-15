

def ScoureStudents(scoure):

    if scoure >100 or scoure < 0:
        return "Invalid"
    if scoure < 50:
        return "Failed"
    if scoure < 65:
        return "Passed"
    if scoure < 75:
        return "Good"
    if scoure < 85:
        return "V.Good"
    if scoure <= 100:
        return "Excellent"
    