#!/bin/python3
# Created by EmanuelFirmino github.com/EmanuelFirmino

from sys import argv, stdout
from urllib import request, error


def banner():
	print( '''
\033[1;49;36m 8""""8           8""""                        
 8    8 e  eeeee  8     eeeee eeeee  eeee eeee 
 8e   8 8  8   8  8eeee 8  88 8   8  8  8 8    
 88   8 8e 8eee8e 88    8   8 8eee8e 8e   8eee 
 88   8 88 88   8 88    8   8 88   8 88   88   
 88eee8 88 88   8 88    8eee8 88   8 88e8 88ee\033[0m

	Usage: dirforce [url] [wordlist_path]

	by: \033[5;49;39mEmanuelFirmino\033[0m

''')

def delete_line():
	stdout.write("\033[F")
	stdout.write("\033[K")

def main():
	with open(argv[0b0010]) as file:
		queue = file.readlines()

	banner()

	for word in queue:
		try:
			url = argv[1] + '/' + word.strip('\n')
			req = request.urlopen(url)
			print(f'\033[1;49;92m***DIRETÓRIO ENCONTRADO!*** URL [{req.url}] STATUS [{req.status}]\033[0m')

		except error.HTTPError:
			print(f'\033[1;49;91m***VERIFICANDO*** {url}\033[0m')
			delete_line()

		except KeyboardInterrupt:
			print('Saindo...')
			break

		except:
			pass

if __name__ == '__main__':
	main() if len(argv) == 0b0011 else banner()
