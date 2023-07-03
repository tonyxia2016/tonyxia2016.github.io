# tonyxia2016.github.io

ffmpeg -i bbb_video_avc_frag.mp4 -vf "scale=1180:664" -c:a copy -movflags frag_keyframe+empty_moov -movflags frag_keyframe+empty_moov bbb_video_avc_frag_1180_664.mp4


1168x656 保证为16的倍数
ffmpeg -i bbb_video_avc_frag.mp4 -vf "scale=1168:656" -c:a copy bbb_video_avc_frag_1168_656.mp4

1152x648 保证为32的倍数

ffmpeg -i bbb_video_avc_frag.mp4 -vf "scale=1152:648" -c:a copy -movflags frag_keyframe+empty_moov bbb_video_avc_frag_1152_648.mp4 这样得到的 bbb_video_avc_frag_1152_648.mp4文件有点大了，再加些参数让它小点

ffmpeg -i bbb_video_avc_frag.mp4 -vf "scale=1152:648" -c:a copy -movflags frag_keyframe+empty_moov -crf 28 bbb_video_avc_frag_1152_648.mp4


540x1280/720=960

960x540

ffmpeg -i bbb_video_avc_frag.mp4 -vf "scale=960:540" -c:a copy -movflags frag_keyframe+empty_moov -crf 28 bbb_video_avc_frag_960_540.mp4

960x544 保证为16的倍数

ffmpeg -i bbb_video_avc_frag.mp4 -vf "scale=960:544" -c:a copy -movflags frag_keyframe+empty_moov -crf 28 bbb_video_avc_frag_960_544.mp4
