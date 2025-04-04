from spleeter.separator import Separator
from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_audio(video_url, output_filename="yt_audio.wav"):
    try:
        yt = YouTube(video_url)
        print(f"🎬 Downloading: {yt.title}")
        
        audio_stream = yt.streams.filter(only_audio=True).first()
        temp_file = audio_stream.download(filename="temp_audio")

        print("🔄 Converting to WAV...")
        audio = AudioSegment.from_file(temp_file)
        audio.export(output_filename, format="wav")

        os.remove(temp_file)
        print(f"✅ Saved as {output_filename}")
        return output_filename

    except Exception as e:
        print(f"❌ Download/Conversion failed: {e}")
        return None

def split_audio(file_path):
    if not os.path.isfile(file_path):
        print(f"❌ File not found: {file_path}")
        return

    separator = Separator('spleeter:2stems')
    print("🎧 Splitting into vocals + instrumental...")
    separator.separate_to_file(file_path, output_path='separated')

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    instrumental_path = os.path.join('separated', base_name, 'accompaniment.wav')
    vocals_path = os.path.join('separated', base_name, 'vocals.wav')

    print("\n🎉 Done!")
    print(f"🎤 Vocals:        {vocals_path}")
    print(f"🎶 Instrumental:  {instrumental_path}")

if __name__ == "__main__":
    url = input("Paste YouTube URL to extract instrumental from: ").strip()
    wav_file = download_youtube_audio(url)

    if wav_file:
        split_audio(wav_file)
