# Creates custom HTTP response header "X-Served-By"

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => inline_template('<%= "Hello World!\n" %>'),
}

exec { 'redirect_me':
  command  => 'sed -i "24i\	\nrewrite ^/redirect_me https://www.youtube.com/v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
}

exec { 'add_header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
  notify   => Service['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
