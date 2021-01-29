# Plex Playlist
Plex Playlist currently generates two playlists from your Plex server; one containing all your songs that were added in the last six months, and another with all songs added in the last two years. You could easily modify or extend this script to generate playlists from a variety of criteria. Having an automated way to generate playlists is great, and using a standard format such as M3U allows you to import the playlist into other media players, or simply back them up.

The purpose of this is so that you can easily find recently added tracks and do things like, I don't know, shuffle them? Play them? Export them? Why does Plex even have the option to view recently added tracks if you can't do anything with them? Anyways, I digress... 


#### System Requirements
* Python 3 and Pip installed
* User access to Plex server

#### Dependency Setup
You will need to install the [Plex API](https://github.com/pkkid/python-plexapi), for example: `pip3 install plexapi`.

## How To Use
Plex Playlist is a python program, executed from the `plex-playlist.py` file. Run the `plex-playlist.py` file with Python 3, adding positional arguments for your server name, section, username and password. Execute the command `python3 plex-playlist.py --help` for more information on running.