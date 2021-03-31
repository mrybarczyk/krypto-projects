Program uruchamia się z dwoma parametrami:
1. Wybór szyfru: -c dla cezara, -a dla afinicznego.
2. -e dla kodowania, -d dla dekodowania, -j dla kryptoanalizy z tekstem jawnym, -k dla kryptoanalizy bez tekstu jawnego.
Parametry można podawać w dowolnej kolejności, ale muszą być dwa, po jednym z wymienionych powyżej grup. Muszą być oddzielone spacją. Aby uzyskać listę wszystkich dostępnych parametrów, można użyć pojedynczego parametru --help.
Przykłady uruchamiania:
	python cezar.py -c -d
	python cezar.py -a -j
	python cezar.py -e -a
	python cezar.py -k -c