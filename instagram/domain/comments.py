class Comments:
    # some initial data for comments, should be changed
    comments = [
        # either "icecave" OR "ice_cave" will satisfy this:
        {'mandatory_words': ["icecave", "ice_cave"],
         'comments': ["Nice shot. Ice caves are amazing", "Cool. Aren't ice caves just amazing?"]},

        # either "high_mountain" OR ("high" AND "mountain") will satisfy this:
        {'mandatory_words': ["high_mountain", ["high", "mountain"]], 'comments': ["I just love high mountains"]},

        # Only ("high" AND "tide" together) will satisfy this:
        {'mandatory_words': [["high", "tide"]], 'comments': ["High tides are better than low"]},

        # Only "summer" AND ("lake" OR "occean") will satisfy this:
        {'mandatory_words': [["summer", ["lake", "occean"]]], 'comments': ["Summer fun"]},

        # Only "summer" AND ("lake" OR "occean") will satisfy this:
        {'mandatory_words': [["poland", ["sea", "ocean"]]],
         'comments': ["Best place in Poland for spending time about sea is Gdańsk!"]},
    ]
