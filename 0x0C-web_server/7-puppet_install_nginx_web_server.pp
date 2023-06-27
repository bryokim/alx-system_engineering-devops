# Installs and configures Nginx server.

include stdlib

exec { 'update':
  command => 'apt-get -yqq update',
  path    => '/usr/bin/:/usr/sbin/:/bin'
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

$string = '
        # 301 redirect for /redirect_me
        location /redirect_me {
                return 301 https://www.youtube.com/v=QH2-TGUlwu4;
        }
}'

file { '/var/www/html/index.html':
  ensure  => present,
  content => inline_template('<%= "Hello World!\n " %>'),
  notify  => Service['nginx'],
  require => Package['nginx']
}

file_line { '301 redirect when quering /redirect_me':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => $string,
  match   => '^}$',
  replace => true,
  notify  => Service['nginx'],
  require => Package['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
