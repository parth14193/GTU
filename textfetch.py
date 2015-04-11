
#!/usr/bin/python

import sys
def fetch():
	counter = 0
	l = []
	l1 = []
	f1 = open('pp.txt','rU')
	f2 = open('pass2.txt','rU')
	for i in f1:
		l.append(i)	
	for j  in f2:
		l1.append(j)
	for k in l:
		if k in l1:
			print k
def main():
	fetch()
main()
