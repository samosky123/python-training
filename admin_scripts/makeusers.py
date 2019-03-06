#!/usr/bin/env python
import subprocess as sub
#
# Create linux accounts pystud1 - pystud14
#
for i in range(1,15):
    pystud = 'pystud' + str(i)
    # sub.call(['userdel', pystud ])
    rc = sub.call(['adduser', pystud ])
    if not rc:
        print "Created account for:", pystud
        # Set passwords
        proc = sub.Popen(['passwd', pystud ], stdout=sub.PIPE, stdin=sub.PIPE, stderr=sub.PIPE)
        resp = pystud + '\n' + pystud
        proc.communicate(resp)
        # chown home directory, don't know why have to do this?
        usergroup = pystud + ':' + pystud
        home = '/home/' + pystud
        sub.call(['chown', usergroup, home])
        # Set sudo
        opt = '-a' + pystud
        sub.call(['gpasswd', opt, 'wheel' ])
