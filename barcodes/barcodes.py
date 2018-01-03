import barcode
from barcode.writer import ImageWriter

for i in range(201):
    if i < 10:
        s = '00'+str(i)
    elif i >= 10 and i < 100:
        s = '0'+str(i)
    else:
        s = str(i)

    barcode.get_barcode_class('code128')(str(i), writer=ImageWriter()).save('pokebar_%s' % (s))
