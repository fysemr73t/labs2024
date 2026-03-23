map2.pdf takes a map and hides it with white square annotation. It's easy to remove this annotation with Apple's preview, and surprisingly difficult to remove it with Acrobat. This shows that there's always another tool to try. 

You should also try to install an open source SVG or PDF editor and see if that works.


photo.pdf is a photo of a well known Harry Potter character. But it's better hidden than with simply by using Preview. We couldn't extract it with Acrobat or with Preview, but we could extract it with an open source tool calle `pdfimages`.

The command line to use is:

pdfimages -j photo.pdf out

