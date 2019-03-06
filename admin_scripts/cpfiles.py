#!/usr/bin/env python
import subprocess as sub
import os
import shutil
#
# Copy all files and sub-directories from /home/pystud16/python-training
# to accounts pystud1 - 14

for i in range(1,15):
    pystud = 'pystud' + str(i)

    src_path = '/home/pystud16/python-training/exercises/'
    src_files = os.listdir(src_path)
    usergroup = pystud + ':' + pystud
    training_path = '/home/' + pystud + '/python-training/'
    exercises_path = training_path + 'exercises/'

    if not os.path.exists(training_path):
        os.makedirs(training_path)
        os.makedirs(exercises_path)
    elif not os.path.exists(exercises_path):
        os.makedirs(exercises_path)

    for file in src_files:
        fqn = src_path + file
        if file.endswith('.py') or file.endswith('.txt') or file.endswith('.rtf'):
            shutil.copy(fqn, exercises_path )
        else:
            # Sub-directory, so create and copy
            sub_path = fqn + '/'
            dst_path = exercises_path + file + '/'
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
            sub_files = os.listdir(sub_path)
            for sub_file in sub_files:
                sub_fqn = sub_path + sub_file
                shutil.copy(sub_fqn, dst_path)
    # Change ownership to local account
    sub.call(['chown', '-R', usergroup, training_path])
