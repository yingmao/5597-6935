# -*- coding:utf-8 -*-

import socket
import time
import json


def get_cpu_status(path='/proc/loadavg'):
    '''
        cpu usage
    '''
    loadavg = {}

    with open(path, 'r') as f1:

        list_content = f1.read().split()

        loadavg['lavg_1'] = list_content[0]

        loadavg['lavg_2'] = list_content[1]

        loadavg['lavg_15'] = list_content[2]

    return loadavg


def get_memory_status(path='/proc/meminfo'):
    '''
       memory usage
    '''
    mem_dic = {}

    with open(path, 'r') as f2:

        lines = f2.readlines()

        for line in lines:

            name = line.strip().split(':')[0]

            data = line.split(":")[1].split()[0]

            mem_dic[name] = float(data)

    return mem_dic
