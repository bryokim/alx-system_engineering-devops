# Automates fixing of a web server

exec {'fix web server':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => 'shell',
}
