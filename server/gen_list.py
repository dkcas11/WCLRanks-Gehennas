#!/usr/bin/python3

import os
import pickle
from pathlib import Path

server_data = {
    "5026": {
        "name" : "Gehennas",
        "userlist" : [],
        "guildlist": ["Nine Nine GDKP"]
    }
}

for server in server_data:
    if not os.path.isdir(server):
        os.mkdir(server)

    pickle.dump(server_data[server]["name"], open('%s/name.pkl' % server, 'wb'))
    if server_data[server]["userlist"]:
        Path(server).mkdir(parents=True, exist_ok=True)
        pickle.dump(server_data[server]["userlist"], open('%s/userlist.pkl' % server, 'wb'))
        print(pickle.load(open('%s/userlist.pkl' % server, 'rb')))
    if server_data[server]["guildlist"]:
        Path(server).mkdir(parents=True, exist_ok=True)
        pickle.dump(server_data[server]["guildlist"], open('%s/guildlist.pkl' % server, 'wb'))
        print(pickle.load(open('%s/guildlist.pkl' % server, 'rb')))

