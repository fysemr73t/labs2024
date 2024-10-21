DIR=lab6
ZIP=$(DIR).zip
FILES=diversityanalysis-orig.pdf *.jpeg map.pdf blank.pdf photo.pdf rti-mdvss-redacted.pdf
$(ZIP):
	(cd .. ; for fn in $(FILES) ; do zip $(ZIP) $(DIR)/$$fn ; done ; ls -l $(ZIP); unzip -l $(ZIP))
	echo 'something hidden in the zip file' | zip -c  ../$(ZIP)
	scp ../$(ZIP) simsong@simson.net:simson.net/$(ZIP)
	ssh simsong@simson.net chmod 644 simson.net/$(ZIP)
	wget https://simson.net/$(ZIP) -O /tmp/$(ZIP)
	cmp ../$(ZIP) /tmp/$(ZIP)
	/bin/rm -f ../$(ZIP) /tmp/$(ZIP)
