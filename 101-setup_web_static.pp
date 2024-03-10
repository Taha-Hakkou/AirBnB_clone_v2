# Redo the task #0 but by using Puppet
exec {'update_packages':
  command  => 'apt -y update && apt -y upgrade',
  provider => 'shell'
}

package {'nginx':
  ensure   => installed,
  provider => 'apt'
}

file {'/data/web_static/shared/':
  ensure => present
}

file {'/data/web_static/releases/test/':
  ensure => present
}

file { '/data/web_static/releases/test/index.html':
  content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>'
}

file {'/data/web_static/current':
  ensure => absent
}

exec {'symlink':
  command  => 'ln -s /data/web_static/releases/test/ /data/web_static/current',
  provider => 'shell'
}

exec {'ownership':
  command  => 'chown -R ubuntu.ubuntu /data/',
  provider => 'shell'
}

exec {'static_alias':
  command  => 'sed -i "s/server_name _;/server_name _;\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}/" \
  /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  restart => 'service nginx restart'
}
