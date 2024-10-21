DIR=lab5
ZIP=$(DIR).zip
$(ZIP):
	(cd .. ; zip $(ZIP) $(DIR)/document*.pdf $(DIR)/sign_with_acrobat.pdf; ls -l $(ZIP); unzip -l $(ZIP))
	scp ../$(ZIP) simsong@simson.net:simson.net/$(ZIP)
	ssh simsong@simson.net chmod 644 simson.net/$(ZIP)
	wget https://simson.net/$(ZIP) -O /tmp/$(ZIP)
	cmp ../$(ZIP) /tmp/$(ZIP)
	/bin/rm -f ../$(ZIP) /tmp/$(ZIP)
