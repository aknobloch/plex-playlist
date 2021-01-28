import sys
from datetime import datetime, timedelta
from util.argparser import get_arg_parser
from plexapi.myplex import MyPlexAccount

if __name__ != "__main__":

    log.error("Plex Playlist not called directly, exiting...")
    sys.exit()

def save_m3u_playlist(file_location, tracks):
    # TODO
    pass

SIX_MONTHS = 31*6
TWO_YEARS = 365*2

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

library_size = 0

for artist in music.searchArtists():
    for track in artist.tracks():
        library_size += 1

        if track.addedAt > six_months_ago:
            six_month_old_tracks += track
            two_year_old_tracks += track
        elif track.addedAt > two_years_ago:
            two_year_old_tracks += track

six_month_old_playlist_title = "six_months_playlist.m3u"
print("Saving six month old playlist as '{}'. It contains {} songs out of the total collection size of {} songs.".format(six_month_old_playlist_title, len(six_month_old_tracks), library_size))
save_m3u_playlist(six_month_old_playlist_title, six_month_old_tracks)

two_year_old_playlist_title = "two_years_playlist.m3u"
print("Saving two year old playlist as '{}'. It contains {} songs out of the total collection size of {} songs.".format(two_year_old_playlist_title, len(two_year_old_tracks), library_size))
save_m3u_playlist(two_year_old_playlist_title, two_year_old_tracks)