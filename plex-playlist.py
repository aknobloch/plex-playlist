import sys
from datetime import datetime, timedelta
from util.argparser import get_arg_parser
from plexapi.myplex import MyPlexAccount

SIX_MONTHS = 31 * 6
TWO_YEARS = 365 * 2

USERVER_PATH_PREFIX = "/mnt/data/aknobloch/files/Music/"
PHONE_PATH_PREFIX = "/storage/emulated/0/Music/"

M3U_HEADER = "#EXTM3U"
M3U_TITLE_TEMPLATE = "#EXTINF:{},{}"

if __name__ != "__main__":

    log.error("Plex Playlist not called directly, exiting...")
    sys.exit()


def save_m3u_playlists(file_location, tracks):
    userver_m3u_content = [M3U_HEADER]
    android_m3u_content = [M3U_HEADER]

    userver_file = "userver_" + file_location
    android_file = "android_" + file_location

    for track in tracks:

        # Get track paths for each platform
        userver_path = track.media[0].parts[0].file
        if (not userver_path.startswith(USERVER_PATH_PREFIX)):
            print("Error! Path name incorrect for {}", userver_path)
            continue
        track_relative_path = userver_path[len(USERVER_PATH_PREFIX):]
        android_path = PHONE_PATH_PREFIX + track_relative_path

        # Create the line items
        line_title = M3U_TITLE_TEMPLATE.format(int(track.duration / 1000),
                                               track.title)
        userver_m3u_content.append(line_title)
        userver_m3u_content.append(userver_path)
        android_m3u_content.append(line_title)
        android_m3u_content.append(android_path)

    # Save each file
    print("Saving uServer file as {}".format(userver_file))
    with open(userver_file, "w") as writer:
        for line_item in userver_m3u_content:
            writer.write(line_item)
            writer.write("\n")

    print("Saving Android file as {}".format(android_file))
    with open(android_file, "w") as writer:
        for line_item in android_m3u_content:
            writer.write(line_item)
            writer.write("\n")


args = get_arg_parser().parse_args()

username = args.user
password = args.password
server_name = args.name
section_name = args.section

account = MyPlexAccount(username, password)
plex = account.resource(server_name).connect()
music = plex.library.section(section_name)

six_months_ago = datetime.now() - timedelta(days=SIX_MONTHS)
six_month_old_tracks = []

two_years_ago = datetime.now() - timedelta(days=TWO_YEARS)
two_year_old_tracks = []

for artist in music.searchArtists():
    for track in artist.tracks():

        if track.addedAt > six_months_ago:
            six_month_old_tracks += track
            two_year_old_tracks += track
        elif track.addedAt > two_years_ago:
            two_year_old_tracks += track

six_month_old_playlist_title = "six_months_playlist.m3u"
save_m3u_playlists(six_month_old_playlist_title, six_month_old_tracks)

two_year_old_playlist_title = "two_years_playlist.m3u"
save_m3u_playlists(two_year_old_playlist_title, two_year_old_tracks)