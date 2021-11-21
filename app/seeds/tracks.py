from app.models import db, Track

def seed_tracks():
    track_1 = Track(user_id=6, album_id=1, genre_id=1, name="Too late", song_url="https://songsforsynthcloud.s3.amazonaws.com/Timecop1983+-+Too+Late+(feat.+LeBrock).mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_2 = Track(user_id=6, album_id=1, genre_id=1, name="Moments in Time", song_url="https://songsforsynthcloud.s3.amazonaws.com/Timecop1983+-+Moments+in+Time.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_3 = Track(user_id=6, album_id=1, genre_id=1, name="It Was Only a Dream", song_url="https://songsforsynthcloud.s3.amazonaws.com/Timecop1983+-+It+was+only+a+Dream.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_4 = Track(user_id=6, album_id=1, genre_id=1, name="Holding on to the Memories", song_url="https://songsforsynthcloud.s3.amazonaws.com/Timecop1983+-+Holding+on+to+the+Memories.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_5 = Track(user_id=6, album_id=1, genre_id=1, name="Alone", song_url="https://songsforsynthcloud.s3.amazonaws.com/Timecop1983+-+Alone.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_6 = Track(user_id=4, album_id=2, genre_id=2, name="Summer of Heat", song_url="https://songsforsynthcloud.s3.amazonaws.com/Summer+of+Heat+(feat.+Kristine).mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_7 = Track(user_id=4, album_id=2, genre_id=2, name="Prime Operator", song_url="https://songsforsynthcloud.s3.amazonaws.com/Prime+Operator.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_8 = Track(user_id=4, album_id=2, genre_id=2, name="Power Move", song_url="https://songsforsynthcloud.s3.amazonaws.com/Power+Move.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_9 = Track(user_id=4, album_id=2, genre_id=2, name="Remember When", song_url="https://songsforsynthcloud.s3.amazonaws.com/Mitch+Murder+-+Remember+When.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_10 = Track(user_id=4, album_id=2, genre_id=2, name="Heading South", song_url="https://songsforsynthcloud.s3.amazonaws.com/Mitch+Murder+-+Heading+South.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_11 = Track(user_id=4, album_id=2, genre_id=2, name="Let Go", song_url="https://songsforsynthcloud.s3.amazonaws.com/Let+Go+(feat.+Anton+Vic)+(Instrumental).mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_12 = Track(user_id=4, album_id=2, genre_id=2, name="Kung Fury", song_url="https://songsforsynthcloud.s3.amazonaws.com/Kung+Fury.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_13 = Track(user_id=5, album_id=3, genre_id=1, name="The Ride", song_url="https://songsforsynthcloud.s3.amazonaws.com/Kalax+-+The+Ride+(Into+The+Midnight)+%5BOfficial+Video%5D.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_14 = Track(user_id=5, album_id=3, genre_id=1, name="Outlands", song_url="https://songsforsynthcloud.s3.amazonaws.com/Kalax+-+Outlands+(HQ).mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_15 = Track(user_id=5, album_id=3, genre_id=1, name="Dream", song_url="https://songsforsynthcloud.s3.amazonaws.com/Kalax+-+Dream.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_16 = Track(user_id=7, album_id=4, genre_id=3, name="Sweetest Romance", song_url="https://songsforsynthcloud.s3.amazonaws.com/Iacon+-+Sweetest+Romance.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_17 = Track(user_id=7, album_id=4, genre_id=3, name="Enjoy Yourself", song_url="https://songsforsynthcloud.s3.amazonaws.com/SAINT+PEPSI+-+ENJOY+YOURSELF+(Music+Video+REUPLOAD).mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_18 = Track(user_id=7, album_id=4, genre_id=3, name="END OF LIFE ENTERTAINMENT SCENARIO #1", song_url="https://songsforsynthcloud.s3.amazonaws.com/SAINT+PEPSI+-+ENJOY+YOURSELF+(Music+Video+REUPLOAD).mp3", image_url="https://i.imgur.com/OvTKGze.jpg")
    track_19 = Track(user_id=5, album_id=3, genre_id=1, name="Dream", song_url="https://songsforsynthcloud.s3.amazonaws.com/Kalax+-+Never+Let+You+Go.mp3", image_url="https://i.imgur.com/OvTKGze.jpg")

    db.session.add(track_1)
    db.session.add(track_2)
    db.session.add(track_3)

    db.session.commit()

def undo_tracks():
    db.session.execute('TRUNCATE tracks RESTART IDENTITY CASCADE;')
    db.session.commit()
