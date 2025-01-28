def metres_to_miles(dist_metres):
    # Calculate the distance in km
    dist_km = dist_metres // 1000

    # Calculate the distance in miles
    dist_miles = 0.621371 * dist_km

    return (dist_miles)

def function_tester(d1,d2,d3):
    dm1 = meters_to_miles(d1)

    assert dm1 == 1.242742, "dm1 incorrect"
    
    dm2 = meters_to_miles(d2)

    assert dm2 == 0.621371, "dm2 incorrect"

    
    dm3 = meters_to_miles(d3)

    assert dm3 == 0.9320565, "dm3 incorrect"





