from FindingStations import stationCalc, hospitalCalc
from gmaps import generateCountyMap

AlamedaStationNum, AlamedaStationAddresses = stationCalc('Alameda','CA')
AlamedaHospitalNum, AlamedaHospAddresses = hospitalCalc('Alameda','CA')

print("Jahsh worked")

'''src, locations = generateCountyMap("3749 Armour Ct, Fremont, CA 94555, US", AlamedaStationAddresses, AlamedaHospAddresses)
print(locations)'''