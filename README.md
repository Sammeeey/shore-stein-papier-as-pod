# shore-stein-papier-as-pod
workflow & script to download all videos from shore-stein-papier on youtube as audio &amp; get rid of intro & outro

1. step: download videos from playlist as audio using yt-dlp package for terminaö (installed via homebrew): https://github.com/ytdl-org/youtube-dl
`yt-dlp -o '%(playlist)s/%(playlist_index)s %(title)s.%(ext)s' 'https://www.youtube.com/playlist?list=PLpr-NGsAGodEbDePSO3wivni39lgdLQjW' -f m4a`

2. step: use python script `trim_audio.py` to cut start & end of audios in directory (install dependencies when asked)
