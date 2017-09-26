#!/usr/bin/env python2.7
#coding=utf-8
#***************************************#
#      -ScriptName: json_read.py-       #
#      -------Author:Matrin------       #
#      --------version:3.0-------       #
#***************************************#

import sys
import os
import json

def location__json(JsonF,LevelName,chars,LJudging_K):
	for location in JsonF[LevelName]:
		if chars in location[LJudging_K]:
			return location

def evaluation_json(ReturnK,JsonF,*location_parameters):
	location_parameter_number = 0
	while len(location_parameters) > location_parameter_number:
		location_parameter_A = location_parameters[location_parameter_number]
		location_parameter_B = location_parameters[location_parameter_number + 1]
		location_parameter_C = location_parameters[location_parameter_number + 2]
		JsonF = location__json(JsonF,location_parameter_A,location_parameter_B,location_parameter_C)
		location_parameter_number = location_parameter_number + 3
		if len(location_parameters) == location_parameter_number:
			if "List" in ReturnK:
				for ReturnV in JsonF[ReturnK]:
					print ReturnV
			else:
				print JsonF[ReturnK]

def enaluation_all(JsonF,enaluation_K):
	if isinstance(JsonF,dict) or isinstance(JsonF,list):
		for x in range(len(JsonF)):
			if isinstance(JsonF,dict):
				temp_key = JsonF.keys()[x]
				temp_value = JsonF[temp_key]
				if temp_key == enaluation_K:
					if isinstance(temp_value,dict) or isinstance(temp_value,list):
						for xx in temp_value:
							if not isinstance(xx,dict) and not isinstance(xx,list):
								print xx
					else:
						print temp_value
				enaluation_all(temp_value,enaluation_K)
			if isinstance(JsonF,list):
				temp_value = JsonF[x]
				enaluation_all(temp_value,enaluation_K)

def main():
	if sys.argv[1] == "-h":
		print "使用方法:\n1.全文取值:\n    ./json_read.py \033[1;32m 要查找value的key \033[0m \033[1;32m 大json文件路径 \033[0m \033[1;32m json文件名 \033[0m \n\n   例如查找所有key为serverList的value\n    ./json_read.py serverList /apsarapangu/disk3/u_disk/ jiuge555.json \n\n2.定位取值:\n    ./json_read.py \033[1;32m 要查找value的key \033[0m \033[1;32m 大json文件路径 \033[0m \033[1;32m json文件名 \033[0m \033[1;32m 一级目录名 \033[0m \033[1;32m 一级目录定位value \033[0m \033[1;32m 一级目录定位key \033[0m \033[1;32m 二级目录名 \033[0m \033[1;32m 二级目录定位value \033[0m \033[1;32m 二级目录定位key \033[0m 以此类推 \n\n   例如查找minirds机器的主机名\n    ./json_read.py serverList /apsarapangu/disk3/u_disk/ jiuge555.json productList minirds-mt productName clusterList maotai clusterName serverRoleGroupList DbMysql serverRoleGroup"
	else:
		JsonF = json.load(open(sys.argv[2] + sys.argv[3]))
		if len(sys.argv) == 4:
			enaluation_all(JsonF,sys.argv[1])
		else:
			evaluation_json(sys.argv[1],JsonF,*sys.argv[4:])


main()
