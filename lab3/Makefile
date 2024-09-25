lab3.zip:
	python3 _make_pdfs.py
	/bin/rm -f lab3.zip
	zip lab3.zip [a-z]*py labfiles/*.pdf
	ls -l lab3.zip
	scp lab3.zip simsong@simson.net:simson.net/lab3.zip
	ssh simsong@simson.net chmod 644 simson.net/lab3.zip
	wget https://simson.net/lab3.zip -O /tmp/lab3.zip
	cmp lab3.zip /tmp/lab3.zip
	/bin/rm -f lab3.zip /tmp/lab3.zip
