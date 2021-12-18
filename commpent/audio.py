import pyaudio
import wave
from tqdm import tqdm

def record_audio(wave_out_path,record_second):
	chuncksize=240
	formats=pyaudio.paInt16
	print(formats)
	channel=1
	rate=8000
	au =pyaudio.PyAudio()
	
	stream =au.open(
		format=formats,
		channels=channel,
		rate=rate,
		input=True,
		frames_per_buffer=chuncksize)

	wf=wave.open(wave_out_path,'wb')
	wf.setnchannels(channel)
	wf.setsampwidth(au.get_sample_size(formats))
	wf.setframerate(rate)
	print("------------------")
	for i in tqdm(range(0,int(rate/chuncksize*record_second))):
		data= stream.read(chuncksize)
		wf.writeframes(data)
	print("------------------")
	stream.stop_stream()
	au.terminate()
	wf.close()
record_audio("./record.wav",4)
