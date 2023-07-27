# WCLRanks Gehennas
An offline Warcraft Logs database intended only for Gehennas EU in WotLK Classic.
See players' ranks immediately without leaving WoW.

The database is updated daily to fetch the latest ranks. 
This means the add-on **DOES NOT** use the internet to display ranks and **DOES NOT** update live.

#### Features
- Shows a players rank in tooltip
- Shows a players rank through shift-clicking in the chat and when they come online
- Supports all current raids
- Configurable information

## Add players to the database
Adding players to the database is very easy.

However currently the only way to add players to the database is through the player's guild. 
To add new players to the database add or change a guild in the `guildlist` list in `server/gen_list.py`. 
Each guild name is surrounded by quotes i.e. `"Nine Nine"` and the list is comma separated.

To add a new guild or change the name of an existing guild you **MUST** submit a [pull request](https://github.com/dkcas11/WCLRanks-Gehennas/pulls) with the guild name as the title of said pull request only. The description can be left empty.
***Do not ask me to modify the list! I will NOT do it for you.***

#### Example of the change
##### Before
```python
server_data = {
    "5026": {
        "name" : "Gehennas",
        "userlist" : [],
        "guildlist": ["Nine Nine"]
    }
}
```

##### After
```python
server_data = {
    "5026": {
        "name" : "Gehennas",
        "userlist" : [],
        "guildlist": ["Nine Nine", "Progress"]
    }
}
```

## Contributing
Contributions are welcome! After all, this add-on is already made possible by community efforts and especially by [AceLan Kao](https://github.com/acelan).
Beware that there is a limit on how much of the WCL API can be used. The free tier provides 4500 points to use the API. These points are used incredibly fast.
The project is currently connected to my personal account with a paid Platinum subscription. However the script that pulls the data is designed to handle the wait for more points to become available each hour but it can only run for a maximum of 6 hours due to the [limit of Github Actions](https://docs.github.com/en/actions/learn-github-actions/usage-limits-billing-and-administration#usage-limits).
Please keep data usage in mind with any changes made to the network requests.

## References
- [WCLRanks](https://github.com/acelan/WCLRanks): Thanks to [AceLan Kao](https://github.com/acelan) for the initial work on his add-on and crawler that made this add-on possible.