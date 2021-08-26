#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

class Cut_nglogs(object):
    __author__ = 'BaoFuQuan'

    def __init__(self,logs):
        self.logfile= logs
        self.__ddict__= { 'Jan': '01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12' }
    
    def cut_logs(self):
        with open(self.logfile,'r') as fr:
            for data in fr.readlines():
                ldt = data.split(sep=" ")[3].split(sep=":")[0][1:]
                ld=self.format_date(ldt)
                flo = 'nginx_access_'+ld+'.log'
                fl = os.getcwd()+'/'+flo
                self.wr_data(fl,data)

    def format_date(self,s):
        ss = s.split(sep='/')
        day = ss[2]+'_'+self.__ddict__[ss[1]]+'_'+ss[0]
        return day
        
    def wr_data(self,fl,ln):
        with open(fl,'a+') as fw:
            fw.write(ln)

if __name__ =='__main__':
    runCut = Cut_nglogs( sys.argv[1] )
    runCut.cut_logs()