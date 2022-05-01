#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    # Write your code here
    """
    case1
    n = len(gene)
    g_list = ['A','C','G','T']
    k = n//4
    t_list = list(gene)
    g_c_list = []
    result = 0
    for i in g_list:
    	cc = t_list.count(i)
    	if cc > k:
    		g_c_list.append(i*(cc-k))
    		result = result + cc - k
    c_len = len(g_c_list)
    print('g_c_list',g_c_list)
    for k in range(result, len(gene)):
    	for s in range(len(gene)):
    		merging = ''.join(sorted(gene[s:s+k]))
    		count = 0
    		for i in g_c_list:
    			if i in merging:
    				count = count + 1
    				if count == len(g_c_list):
    					return k
    		if s + result > len(gene):
    			continue
    """
    """
    case2
    n = len(gene)
    g_list = ['A','C','G','T']
    t_list = list(gene)
    k = n//4
    g_c_list = []
    result = 0
    for i in g_list:
    	cc = t_list.count(i)
    	g_c_list.append(cc)
    	if cc > k:
    		result = result + cc - k
    finish = False
    while finish != True:
    	for i in range(len(gene) - result):
    		s_list = list(gene[i:i+result])
    		s_c_list = []
    		for j in g_list:
    			s_c_list.append(s_list.count(j))
    		c_list = []
    		for s in range(len(g_list)):
    			c_list.append(g_c_list[s] - s_c_list[s])
    		for j in c_list:
    			if j > k:
    				finish = False
    				break
    			else:
    				finish = True
    		if finish == True:
    			break
    	if finish == False:
    		result = result + 1
    return result
    """
    dic = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in gene:
    	dic[i] += 1
    x = len(gene)
    n = x / 4
    i = 0
    j = 0
    mins = x
    if dic['A'] == n and dic['T'] == n and dic['C'] == n and dic['G'] == n:
    	return 0
    else:
    	while i < x and j < x:
    		while (dic['A'] > n or dic['C'] > n or dic['T'] > n or dic['G'] > n) and i < x:
    			dic[gene[i]] -= 1
    			print('i',i)
    			i += 1
    			print('dic i',dic)
    		while dic['A'] <= n and dic['C'] <= n and dic['T'] <= n and dic['G'] <= n:
    			dic[gene[j]] += 1
    			print('j',j)
    			j += 1
    			print('dic j',dic)
    		if i - j < mins:
    			mins = i - j + 1
    	return mins




if __name__ == '__main__':

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    print(result)
