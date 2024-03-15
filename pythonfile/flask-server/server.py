from flask import Flask,jsonify,request,send_file
from moviepy.editor import VideoFileClip
from flask_cors import CORS

app=Flask( __name__)
CORS(app)



@app.route('/converter',methods=['POST'])
def converter():
    if 'video' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    video_file = request.files['video']
   
   
    video_file.save('input_video.mp4')
   
    
    video = VideoFileClip('input_video.mp4')

    audio = video.audio
    
    audio_path = "output_audio.mp3"
    audio.write_audiofile( audio_path)
    
    
    return send_file(audio_path,as_attachment=True)


if __name__=="__main__":
    app.run(debug=True)