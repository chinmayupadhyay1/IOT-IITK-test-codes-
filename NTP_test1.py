import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('in.pool.ntp.org', version=3)
response.offset
print (ctime(response.tx_time))
print (ntplib.ref_id_to_text(response.ref_id))

x = ntplib.NTPClient()
print ((x.request('ch.pool.ntp.org').tx_time))
