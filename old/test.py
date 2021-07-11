from FindingStations import stationCalc, hospitalCalc
from gmaps import generateCountyMap

print("started")

AlamedaStationNum, AlamedaStationAddresses, AlamedaStationNames = stationCalc('Alameda','CA')
AlamedaHospitalNum, AlamedaHospitalAddresses, AlamedaHospitalNames = hospitalCalc('Alameda','CA')

print("Jahsh worked")

src, locations = generateCountyMap("3749 Armour Ct, Fremont, CA 94555, US", AlamedaStationAddresses, AlamedaHospitalAddresses,\
                                   AlamedaStationNames, AlamedaHospitalNames)
print(locations)

print("Anuj Worked")
