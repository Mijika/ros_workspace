import math


def lla_to_ecef(lat, lon, alt):
	"""Convert LLA to ECEF

	Convert to ECEF with Latitude and Longitude

	Arguments:
		lat {flaot} -- [latitude]
		lon {flaot} -- [longitude]
		alt {flaot} -- [altitude]

	return:
		x {flaot} -- [x]
		y {flaot} -- [y]
		z {flaot} -- [z]

	"""

	rad_lat = math.radians(lat)
	rad_lon = math.radians(lon)

	a = 6378137.0
	finv = 298.257223563
	f = 1 / finv
	e2 = 1 - (1 - f) * (1 - f)
	v = a / math.sqrt(1 - e2 * math.sin(rad_lat) * math.sin(rad_lat))

	x = (v + alt) * math.cos(rad_lat) * math.cos(rad_lon)
	y = (v + alt) * math.cos(rad_lat) * math.sin(rad_lon)
	z = (v * (1 - e2) + alt) * math.sin(rad_lat)

	return (x, y, z)


if __name__ == '__main__':
	lat = 37.484305
	lon = 126.9938894
	alt = 65.155

	print(lla_to_ecef(lat, lon, alt))

