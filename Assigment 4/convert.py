def kilometers_to_meters( km ):
    return km*1000
    print(f"{a} meters")

def Meters_to_Centimeters( m ):
     return m*100
     print(f"{a} centimeters")
    
def centimeters_to_millimeters( cm ):
     return cm*10
     print(f"{a} millimeters")

def feets_to_inches( ft ):
     return ft*12
     print(f"{a} inches")

def inches_to_centimeter( inch ):
     return inch*2.54
     print(f"{a} centimeter")



def distance_converter(distance, conversion_type,conversion_func):
 result=conversion_func(distance)
 print(f"{conversion_type}:{result}")  
    
value = float(input("Enter a distance value: "))

print("\nConverted Values:")

distance_converter(value, "Kilometers to Meters (km → m)", kilometers_to_meters)
distance_converter(value, "Meters to Centimeters (m → cm)", Meters_to_Centimeters)
distance_converter(value, "Centimeters to Millimeters (cm → mm)", centimeters_to_millimeters)
distance_converter(value, "Feet to Inches (ft → in)", feets_to_inches)
distance_converter(value, "Inches to Centimeters (in → cm)",inches_to_centimeter)
        