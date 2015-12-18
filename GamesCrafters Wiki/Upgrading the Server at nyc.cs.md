Upgrading the Server at nyc.cs
==============================

Log of the nyc.cs.berkeley.edu laptop update on 2009-09-21:

1.  Full backup of MySQL DB dumped, archived, compressed, and transferred to the gamers account on Inst. The database dump includes the data for the GC Wiki and Fogbugz.
2.  Fogbugz application code and backups moved to gamers account on OCF.
3.  Resized the partition containing the old Fedora 6 server files to 19.3GB. It is a logical volume (LVM) in VolGroup00 on /dev/sda2.
4.  Installed Fedora 11 on /dev/sda3 with 37GB of space. /dev/sda1 was kept as the boot partition. Created a non-admin account called gamers. Muted the speakers.
5.  Updated all packages. Exactly 400 updates and 90 minutes later…
6.  Used the System -&gt; Administration -&gt; Services tool to Enable and also Start the httpd and sshd services.
7.  Installed MySQL server and client (mysql-server and mysql versions 5.1.37-1.fc11)
8.  Again, used the Service tool to Enable and Start mysqld.
9.  Installed emacs.
10. Supressed SELinux by setting SELINUX=permissive in /etc/selinux/config
11. Installed php-5.2.9, php-mysql, and php-pdo (including all dependencies). Restarted the server with /sbin/service httpd graceful
12. Downloaded Tomcat from the Apache site and extracted it to /opt. Symlinked apache-tomcat to the extracted apache-tomcat -6.0.20 directory. Added the line su gamers /opt/apache-tomcat/bin/startup.sh to /etc/rc.local. Used chown to make the gamers account the owner.
13. Installed subversion and ant.
14. Checked out GamesmanJava and GamesmanWeb into /home/gamers. Built both of them with ant. Deployed GamesmanWeb with launch.sh.
15. Used System-&gt;Administration-&gt;Firewall to open up ports 80 (WWW HTTP), 443 (Secure WWW HTTPS), and using the Other Ports option, 8080 (this is what Tomcat listens on). You could probably disable the entire firewall and make your life easier, instead.
16. To import the database dump, ran mysql -u root &lt; backup.sql
17. Copied wiki files into /var/www/wiki
18. Copied Fogbugz files to /opt/fogbugz. Installed php-pear, php-pear-Mail, php-pear-Mail-Mime, and php-pear-Mail-mimeDecode, which Fogbugz requires.
19. Created /opt/httpd/conf.d/fogbugz.conf with the contents:

`#Automatically added by FogBUGZ`
`#Include /opt/fogbugz/Accessories/fogbugz.conf`
`Alias /fogbugz /opt/fogbugz/Website`
`<Directory "/opt/fogbugz/Website">`
`  Options All`
`  AllowOverride All`
`  Allow from All`
`  Order Allow,Deny`
`  DirectoryIndex default.php`
</Directory>
`#Automatically added by FogBUGZ`
