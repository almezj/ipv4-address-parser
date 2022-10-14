def parse_ipv4(dot_notation: str) -> int:
	components = dot_notation.split(".")
	if len(components) != 4:
		raise ValueError("Invalid IPv4: " + dot_notation)
	

	result = 0
	for components in components:
		component_as_int = int(components)
		if not 0 <= component_as_int <=255:
			raise ValueError("Invalid IPv4: " + dot_notation)


		result <<= 8
		result |= component_as_int

	return result

def format_ipv4(adress: int) -> str:
	if adress > 0xFFFFFFFF:
		raise ValueError("IPv4 adress too large: " + str(adress))
	b1 = (adress >> 24) & 0xFF
	b2 = (adress >> 16) & 0xFF
	b3 = (adress >> 8) & 0xFF
	b4 = (adress >> 0) & 0xFF

	return f"{b1:d}.{b2:d}{b3:d}.{b4:d}"

def create_mask(bits: int) -> int:
	if not 0 <= bits <= 32:
		raise ValueError("Invalid mask length: " + str(bits))

	return (0xFFFFFFFF << (32 - bits))


#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

cidr = input("IPv4 Adress [CIDR]: ")
cidr_components = cidr.split("/")
if len (cidr_components) != 2:
	print("ERROR Invalid CIDR!")
	exit(-1)


try:
	host_adress = parse_ipv4(cidr_components[0])
except ValueError:
	print("ERROR Invalid IPv4 notation!")
	exit(-1)

try:
	mask_bits = int(cidr_components[0])
except ValueError:
	print("ERROR: Invalid IPv4 notation!")
	exit(-1)


