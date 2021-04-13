<?php
   // Dates
   echo date('d'); // Day 
   echo date('m'); // Month 
   echo date('Y'); // Year
   echo date('l'); // Day of the Week

   echo date('Y/m/d');
   echo date('d-m-y');

   echo date('h'); // Hour
   echo date('i'); // Min
   echo date('s'); // Seconds
   echo date('a'); // AM or PM 

   // Setting the time zone 7
   date_default_timezone_get('England');

   echo date('h:i:sa');

   // timestamps 
   $timestamp = mktime(10, 14, 54, 9, 10 ,1980);
   echo $timestamp;


?>