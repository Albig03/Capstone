from spleeter.separator import Separator
import os

def split_audio(file_path):
    if not os.path.isfile(file_path):
        print(f"❌ File not found: {file_path}")
        return

    # Create a Spleeter separator for 2 stems (vocals + accompaniment)
    separator = Separator('spleeter:2stems')

    print("🔄 Splitting audio...")
    separator.separate_to_file(file_path, output_path='separated')

    # Paths to the output files
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    instrumental_path = os.path.join('separated', base_name, 'accompaniment.wav')
    vocals_path = os.path.join('separated', base_name, 'vocals.wav')

    print(f"\n✅ Done splitting!\n🎶 Instrumental: {instrumental_path}\n🎤 Vocals: {vocals_path}")

if __name__ == "__main__":
    file_path = input("Enter the path to your song file (e.g. song.mp3): ").strip()
    split_audio(file_path)
