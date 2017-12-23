# -*- coding: utf-8 -*-
"""
Create date: 2017-07-17
@Author : zengbin
A tool for init ubuntu.
"""

import os
import subprocess

wdir = '/home/bzeng/Downloads'

def prepare_env():
    install = 'sudo apt-get install '
    os.system(install + 'vim')
    os.system(install + 'openssh-server')

def batch_download(path=wdir):
    """batch download files needed"""
    os.chdir(path)
    download_lists = {
                'Hadoop 2.7.3': 'https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-2.7.3/hadoop-2.7.3.tar.gz',
                'Hive 2.1.1': 'https://mirrors.tuna.tsinghua.edu.cn/apache/hive/hive-2.1.1/apache-hive-2.1.1-bin.tar.gz',
                'Spark 2.2.0': 'https://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-2.2.0/spark-2.2.0-bin-hadoop2.7.tgz',
                'Hbase 1.2.6': 'https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/stable/hbase-1.2.6-bin.tar.gz',
                'Pig 0.17': 'https://mirrors.tuna.tsinghua.edu.cn/apache/pig/latest/pig-0.17.0.tar.gz',
                'jdk 8u131': 'http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz',
    }

    for key, url in download_lists.items():
        print('current downloading: %s' % key)
        os.system('nohup wget ' + url + '&')

    os.chdir(wdir)


def batch_decompress():
    """"""
    pass

"""
-------------------------------------------------------------------------------
Install Docker on Ubuntu 16.04
-------------------------------------------------------------------------------
"""
cmd1 = 'apt-get update'
cmd2 = 'apt-get install apt-transport-https ca-certificates'
cmd3 = 'apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D'
cmd4 = ''
p = subprocess.run(cmd1.split(' '))



"""
-------------------------------------------------------------------------------
Install MongoDB on Ubuntu 16.04
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
-------------------------------------------------------------------------------
"""
cmd = 'su'
# step 1. Import the public key used by the package management system.
mongodb_cmd1 = 'sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6'
# step 2. Create a list file for MongoDB.
mongodb_cmd2 = 'echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list'
# step 3. Reload local package database.
mongodb_cmd3 = 'sudo apt-get update'
# step 4. Install the MongoDB packages.
mongodb_install = 'sudo apt-get install -y mongodb-org'
