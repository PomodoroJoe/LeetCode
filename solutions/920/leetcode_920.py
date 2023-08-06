#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime: 100.00%
# Memory:   31.60%


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:

        @cache
        def numMusicPlaylistsRecurse(song_count, unique_song_count):
            if song_count == goal:
                if unique_song_count == n:
                    return 1
                return 0

            # Option 1: add a unique song
            option_1 = 0

            unique_songs_remaining = n - unique_song_count
            if unique_songs_remaining > 0:
                option_1 = numMusicPlaylistsRecurse(song_count + 1, unique_song_count + 1)
                option_1 *= unique_songs_remaining


            # Option 2: add a repeat song
            option_2 = 0

            if song_count > k:
                option_2 = numMusicPlaylistsRecurse(song_count + 1, unique_song_count)

                # how many songs can we repeat?
                available_song_count = unique_song_count - k
                option_2 *= available_song_count

            return option_1 + option_2

        return numMusicPlaylistsRecurse(0, 0) % (10**9 + 7)