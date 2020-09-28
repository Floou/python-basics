#1
#row_record = '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
#correct_request_IP_address = '217.168.17.5'
#correct_request_datetime = '17/May/2015:08:05:12'

#request_IP_address = row_record.split()[0]
#request_datetime = row_record.split()[4]
#print(request_IP_address, ", ", request_datetime)

#assert request_IP_address == correct_request_IP_address
#assert request_datetime == correct_request_datetime

#2*
#row_record = '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
#correct_request_IP_address = '217.168.17.5'
#correct_request_datetime = '17/May/2015:08:05:12'
#correct_request_method = 'GET'
#correct_requested_resource = '/downloads/product_2'

#request_IP_address = row_record.split()[0]
#request_datetime = row_record.split()[4]
#request_method = row_record.split()[6]
#requested_resource = row_record.split()[7]
#print(request_IP_address, ", ", request_datetime, ", ", request_method, ", ", requested_resource)

#assert request_IP_address == correct_request_IP_address
#assert request_datetime == correct_request_datetime
#assert request_method == correct_request_method
#assert requested_resource == correct_requested_resource

'''
217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"
1. [<remote_IP_address>, <request_datetime>]
*2. [<remote_IP_address>, <request_datetime>, <request_method>, <requested_resource>]
['217.168.17.5', '17/May/2015:08:05:12 +0000', 'GET', '/downloads/product_2']
3. print parsed log
'''
