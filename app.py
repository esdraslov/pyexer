import detector as dt

while True:
    port = dt.detect()
    if port:
        print('hi')