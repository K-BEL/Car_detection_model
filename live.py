import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO(r"C:\Users\k.belhadj\Desktop\Car_detection_model\weights\best.pt")  # Replace with your model

# Stream URL
stream_url = "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1733863115/ei/a1JYZ-G5FejHmLAPtpiJwQg/ip/105.157.105.147/id/w2gG6XjN1qk.5/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/rqh/1/hdlc/1/hls_chunk_host/rr4---sn-p5h-gc5y.googlevideo.com/xpc/EgVo2aDSNQ%3D%3D/playlist_duration/30/manifest_duration/30/vprv/1/playlist_type/DVR/initcwndbps/617500/met/1733841515,/mh/1B/mip/41.140.41.169/mm/44/mn/sn-p5h-gc5y/ms/lva/mv/m/mvi/4/pl/24/rms/lva,lva/dover/11/pacing/0/keepalive/yes/fexp/51326932,51331020,51335594,51347747/mt/1733840917/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,rqh,hdlc,xpc,playlist_duration,manifest_duration,vprv,playlist_type/sig/AJfQdSswRQIhAPzv76w8rEfC0tnAoB3abu1R5ElzEnilmcHKfmq46bH3AiBP15mmWs0niHH3qsJqgMQrjcKp7BIwSJ5dOsgbC_1Nbw%3D%3D/lsparams/hls_chunk_host,initcwndbps,met,mh,mip,mm,mn,ms,mv,mvi,pl,rms/lsig/AGluJ3MwRgIhALpUqeuXIBY7MRZMy_xFeEZTJpLk-rHi_E0g7u-ivIeaAiEA09h5zEXsucbRddB7wzFlk14794h_7NFGGCz8n3vLlZY%3D/playlist/index.m3u8"

cap = cv2.VideoCapture(stream_url)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to read from stream. Retrying...")
        continue

    # Perform YOLO detection
    results = model(frame)

    # Annotate each frame
    for result in results:
        annotated_frame = result.plot()  # Use .plot() to draw the detections on the frame

    # Display the annotated frame
    cv2.imshow("YOLO Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
