import datetime
import os
from itertools import combinations
from functools import reduce
import math
import sys
from random import shuffle
import numpy as np


record = None
server_num, client_num, time_len = 0, 0, 0
pressure = 0.3
qos_lim = 0
qos = None
dist_matrix = None

def ask(msg: str, default: int):
    inputed = input(msg)
    if inputed.strip():
        return int(inputed.strip())
    return default

def read_input():
    global server_num, client_num, time_len, pressure
    server_num = ask('input server number (default 100):', 100)
    client_num = ask('input client number (default 30):', 30)
    time_len = ask('input time length (default 1000):', 1000)
    inp = input('input pressure 0.01-0.99 (default 0.3):')
    if inp.strip():
        pressure = float(inp.strip())

def distribute_server():
    global record, qos_lim, qos
    qos_lim = np.random.randint(150, 300)
    offset = np.random.randint(10, 50)
    qos = np.ceil(np.random.normal(qos_lim+offset, 50, size=(server_num, client_num))).astype('int32')
    mask = np.random.randn()
    for t_idx in range(time_len):
        dis_bd = np.random.randint(0, math.ceil(550000 / client_num / 37), size=(server_num, client_num)) * (qos < qos_lim)
        mask = np.abs(np.random.randn(server_num, client_num)) > 0.27
        dis_bd = dis_bd * mask
        record[t_idx] = dis_bd

def gen_client_name(n: int):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    out = list(combinations(alphabet, 2))
    out = [ reduce(lambda x, y: x+y, each) for each in out ]
    out += [ i for i in alphabet ]
    shuffle(out)
    out = out[:n]
    out.sort()
    return out

def gen_server_name(n: int):
    cand = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
    out = list(combinations(cand, 2))
    out = [ reduce(lambda x, y: x+y, each) for each in out ]
    shuffle(out)
    out = out[:n]
    out.sort()
    return out

def output(path: str):
    curr_time = datetime.datetime(2021, 11, 1, 0, 0)
    time_sep = datetime.timedelta(minutes=5)
    sname = gen_server_name(server_num)
    cname = gen_client_name(client_num)
    with open(os.path.join(path, 'demand.csv'), 'w', newline='') as f:
        f.write('mtime,' + ','.join(cname) + '\r\n')
        for t_idx in range(time_len):
            time_str = curr_time.strftime("%Y-%m-%dT%H:%M")
            c_demand = record[t_idx].sum(axis=0)
            zero_mask = np.abs(np.random.randn(client_num))
            zero_mask = zero_mask > 1e-2
            c_demand *= zero_mask
            c_demand = [ str(i) for i in c_demand ]
            f.write(time_str + ',' + ','.join(c_demand) + '\r\n')
            curr_time += time_sep
    with open(os.path.join(path, 'site_bandwidth.csv'), 'w', newline='') as f:
        f.write('site_name,bandwidth\r\n')
        for s_idx in range(server_num):
            bd_used = record.sum(axis=-1)[:, s_idx].max()
            bd_upper = np.ceil(bd_used / pressure).astype('int32')
            f.write(f'{sname[s_idx]},{bd_upper}\r\n')
    with open(os.path.join(path, 'qos.csv'), 'w', newline='') as f:
        f.write('site_name,' + ','.join(cname) + '\r\n')
        for s_idx in range(server_num):
            s = sname[s_idx]
            qos_list = qos[s_idx]
            qos_list = [ str(i) for i in qos_list ]
            qos_str = ','.join(qos_list)
            f.write(f'{s},{qos_str}\r\n')
    with open(os.path.join(path, 'config.ini'), 'w', newline='') as f:
        f.write('[config]\r\n')
        f.write(f'qos_constraint={qos_lim}\r\n')

if __name__ == '__main__':
    read_input()
    record = np.zeros((time_len, server_num, client_num), dtype=np.int32)
    distribute_server()
    if len(sys.argv) == 1:
        output('simulated_data')
    else:
        try: os.mkdir(sys.argv[1])
        except: pass
        output(sys.argv[1])
    
