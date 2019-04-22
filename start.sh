#!/data/data/com.termux/files/usr/bin/sh
proot -0 -r ~/stable -b /dev/ -b /sys/ -b /proc/ -b /data/data/com.termux/files/home /usr/bin/env -i HOME=/root TERM="xterm-256color" PS1='[root@stable \W]$ ' PATH=/bin:/usr/bin:/sbin:/usr/sbin:/bin /bin/bash --login
