# tee ratkaisu tänne
def ilman_vokaaleja(mjono):
	mjono = mjono.replace('a', '')
	mjono = mjono.replace('e', '')
	mjono = mjono.replace('i', '')
	mjono = mjono.replace('o', '')
	mjono = mjono.replace('u', '')
	mjono = mjono.replace('y', '')
	mjono = mjono.replace('ä', '')
	mjono = mjono.replace('ö', '')
	mjono = mjono.replace('å', '')
	return mjono

if __name__ == '__main__':
	mjono = "tämä on esimerkki"
	print(ilman_vokaaleja(mjono))