fx_version 'cerulean'
games { 'rdr3', 'gta5' }

author 'Vincent (Vincent.#8539 - Discord)'
description 'Axotic Anti-Cheat'
version '1.0.0'

ui_page 'src/index.html'

files { 
'configs/client_config.lua',
'configs/server_config.lua',
'src/index.html', 
'src/index.css'
}

client_scripts {
    'client.lua',
    'src/index.js',
    'client.cs'
}

server_scripts {
    '@mysql-async/lib/MySQL.lua',
    'configs/server_config.lua',
    'server.lua',
    'src/server.js'
}
