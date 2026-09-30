"""
Music Library Module for JARVIS Voice Assistant
Stores curated YouTube links and provides song lookup utilities.
"""

music = {
    "jazz": "https://youtu.be/_biYHnOtF0g?si=YoPeGf2plxX9rRua",
    "twinkle twinkle": "https://youtu.be/dgz0KjnW21M?si=7BsL0J7wMTKDREsn",
    "snake on the beach": "https://youtu.be/dgz0KjnW21M?si=_7Xvs8AcgmfxTXyK",
    "ba ba black sheep": "https://youtu.be/MR5XSOdjKMA?si=Drhhz8i2sA_-fzre",
    "baba baba black ship": "https://youtu.be/MR5XSOdjKMA?si=Drhhz8i2sA_-fzre",
    "hathi raja kahan chale": "https://youtu.be/gAM6v3BkjYE?si=4bo9fZz-UbWNfnLs",
    "bike rides": "https://youtu.be/rfBc1csPgMI?si=XwHf8f8uH0i5gT2F",
    "lofi": "https://www.youtube.com/watch?v=jfKfPfyJRdk",
    "chill": "https://www.youtube.com/watch?v=5qap5aO4i9A",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
}

def get_music_url(song_name: str):
    """
    Search for a song in the library using case-insensitive lookup.
    Returns the URL if found, else None.
    """
    if not song_name:
        return None
    
    clean_name = song_name.strip().lower()
    
    # Direct match
    if clean_name in music:
        return music[clean_name]
    
    # Partial match
    for title, url in music.items():
        if clean_name in title or title in clean_name:
            return url
            
    return None