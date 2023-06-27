# Installs and configures Nginx server.

include stdlib

exec { 'update':
  command => 'apt-get -yqq update',
  path    => '/usr/bin/:/usr/sbin/:/bin'
}
~> package { 'nginx':
  ensure  => installed,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

$string = '
        # 301 redirect for /redirect_me
        rewrite ^/redirect_me$ https://youtube.com/v=QH2-TGUlwu4 permanent;
}'

file_line { '301 redirect when quering /redirect_me':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => $string,
  match   => '^}$',
  replace => true,
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  hasrestart => true,
  require    => Package['nginx'],
}
