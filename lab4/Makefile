lab4.zip:
	cd .. ; zip lab4.zip lab4/*.docx lab4/*.pptx lab4/*.py lab4/*.txt
	ls -l ../lab4.zip
	scp ../lab4.zip simsong@simson.net:simson.net/lab4.zip
	ssh simsong@simson.net chmod 644 simson.net/lab4.zip
	wget https://simson.net/lab4.zip -O /tmp/lab4.zip
	cmp ../lab4.zip /tmp/lab4.zip
	/bin/rm -f ../lab4.zip /tmp/lab4.zip
