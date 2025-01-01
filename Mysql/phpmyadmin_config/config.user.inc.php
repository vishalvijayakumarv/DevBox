<?php
/*
* First server
*/
$i++;
/* Authentication type */
$cfg['Servers'][$i]['auth_type'] = 'cookie';
/* Server parameters */
$cfg['Servers'][$i]['verbose'] = 'mysql-container';
$cfg['Servers'][$i]['host'] = 'mysql';
$cfg['Servers'][$i]['connect_type'] = 'tcp';
$cfg['Servers'][$i]['compress'] = false;
/* Select mysqli if your server has it */
$cfg['Servers'][$i]['extension'] = 'mysql';
$cfg['Servers'][$i]['port']          = '3306';
$cfg['Servers'][$i]['AllowNoPassword'] = false;

/*
* 2nd server
we can add more connections same as below 
*/

//$i++;
/* Authentication type */
//$cfg['Servers'][$i]['auth_type'] = 'cookie';
/* Server parameters */
//$cfg['Servers'][$i]['verbose'] = 'Mysql_3306';
//$cfg['Servers'][$i]['host'] = '172.22.0.4';
//$cfg['Servers'][$i]['connect_type'] = 'tcp';
//$cfg['Servers'][$i]['compress'] = false;
/* Select mysqli if your server has it */
//$cfg['Servers'][$i]['extension'] = 'mysql';
//$cfg['Servers'][$i]['AllowNoPassword'] = false;

