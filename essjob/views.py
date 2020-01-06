from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import os
import os.path
import request
import requests
import json
from requests.auth import HTTPDigestAuth
#import cx_Oracle
import re

def essjob(request):
	'''
	print(request)
	path1=request.body
	my_json = path1.decode('utf8').replace("'", '"')
	print(my_json)
	data1 = json.loads(my_json)
	file= data1['fileName']'''
	'''
	con = cx_Oracle.Connection("shubhver/Rtyuiop@2019@uerdx8001-vip.us.oracle.com:1554/ALPHA_ADHOC.us.oracle.com")
	cursor = con.cursor()
	a = cursor.execute("""Select * from ra_interface_lines_all where interface_line_attribute1='33502039'""")
	print(a)'''
	S0=''
	S1=''
	S2=''
	S4=''
	S5='' 


	BusinessUnitIds = 300001096431127
	BatchSourceIds  = 300001107407671
	sysdate = 2019-12-27
	fromDate = 'null'
	ToDate = 'null'

		

	url="https://efip-dev1.fa.us6.oraclecloud.com:443/fscmService/ErpIntegrationService"
	headers = {'content-type': 'text/xml'}

	xmlfile = open('test.xml','r')
	body = xmlfile.read()
	response = requests.post(url, data=body.format(BusinessUnitIds=BusinessUnitIds, BatchSourceIds=BatchSourceIds, sysdate=sysdate,fromDate=fromDate,ToDate=ToDate), headers=headers,auth=('oalo2c_ww@oracle.com', 'Owcw2!365'))
	
	my_string = response.content.decode('utf-8')
	my_string_result_start_index = my_string.rfind('<result')
	my_string_result_end_index = my_string.rfind('result>')
	final_string = my_string[my_string_result_start_index : my_string_result_end_index]
	final_output =  re.findall(r'\d+', final_string)
	
	final_keys=['Job_ID']
	combo=zip(final_keys,final_output)
	final_result=json.dumps(dict(combo))
	
	return HttpResponse(final_result)
