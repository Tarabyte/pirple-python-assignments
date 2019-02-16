"""
Variables assignment
What's your favorite song?

Think of all the attributes that you could use to describe that song.
"""
# Song Title
Song = "Yesterday"

# Artist
Artist = "The Beatles"

# Duration
DuractionInSeconds = 123
# Minutes and Seconds
(DurationMinutes, DuractionSeconds) = divmod(DuractionInSeconds, 60)

# Album
AlbumName = "Help!"

# Production Info
Label = "Capitol"

"""
Recorded Date
"""
RecordedYear, RecordedMonth, RecordedDay = 1965, "June", 14

"""
Released Date
"""
ReleasedYear, ReleasedMonth, ReleasedDay = 1965, "September", 13


# print info
print("---- Song Info ----\n")
print("Song Name: {0}".format(Song))
print("Artist: {0}".format(Artist))
print("Duration: {0}:{1:02d} ({2} seconds)".format(
    DurationMinutes, DuractionSeconds, DuractionInSeconds))
print("From Album: {0}".format(AlbumName))

print("\n---- Production Info ----\n")
print("Label: {0}".format(Label))
print("Record Date: {} {}, {}".format(
    RecordedDay, RecordedMonth, RecordedYear))
print("Release Date: {} {}, {}".format(
    ReleasedDay, ReleasedMonth, ReleasedYear))
