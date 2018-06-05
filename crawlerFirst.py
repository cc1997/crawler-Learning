#-*-coding:utf-8-*-
import re
import requests
import time
url = 'http://www.cqksw.org/StudentAssessment/TestPaper'
params = {
	'cId':'00b4b408-4ca4-4143-a61a-60c4b84c6fcd',
	'modelType':'modelType0',
	'moduleType':'moduleType00',
	'qNum':'12'
}
res_test1=r'<span>(.*?)</span>'

for num in range(0,106):
	numx = str(num)
	params['qNum'] = numx
	r = requests.get(url,params)
	res_test1=r'<span>(.*?)</span>'
	m_test1=re.findall(res_test1,r.text,re.S|re.M)
	print(m_test1)
	#sys.stdout.flush()
	time.sleep(10)

#for num in range(0,106):
#	numx = str(num)
#	params['qNum'] = numx
#	r = requests.get(url,params)
#	print(num)
#	res_test1=r'<span>(.*?)</span>'
#	m_test1=re.findall(res_test1,r.text,re.S|re.M)
#	print(m_test1[5])
#	m_test2=re.findall(res_test2,r.text,re.S|re.M)
#	print(m_test2[0])
#	if (m_test2[0])=='A':
#		res_test3=r'<label><input class="studentAnswer" name="studentAnswer" type="radio" value="A" title="A" checked/>(.*?)</label>'
#	elif (m_test2[0])=='B':
#		res_test3=r'<label><input class="studentAnswer" name="studentAnswer" type="radio" value="B" title="B"/>(.*?)</label> '
#	elif (m_test2[0])=='C':
#		res_test3=r'<label><input class="studentAnswer" name="studentAnswer" type="radio" value="C" title="C"/>(.*?)</label> '
#	else:
#		res_test3=r'<label><input class="studentAnswer" name="studentAnswer" type="radio" value="D" title="D"/>(.*?)</label> '
#	m_test3=re.findall(res_test3,r.text,re.S|re.M)
#	print(m_test3)
#	print('\n')
#	#sys.stdout.flush()
#	time.sleep(3)	
