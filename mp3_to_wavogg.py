#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydub import AudioSegment
import os, glob, sys


root_mp3_path = 'indec_mp3'
root_output = 'audios'
wav_path = os.path.join(root_output, 'wav')
ogg_path = os.path.join(root_output, 'ogg')
mp3_path = os.path.join(root_output, 'mp3')


def main(folder = root_mp3_path, files_type ='*.mp3'):
	for mp3 in glob.glob(os.path.join(folder, files_type) ):
	# for mp3 in mp3s:
		""" convert mp3 to wav """
		wav_name =  mp3.split('/')[-1].replace('.mp3', '.wav')
		ogg_name =  mp3.split('/')[-1].replace('.mp3', '.ogg')
		mp3_name = mp3.split('/')[-1]
	
		src_mp3 = os.path.join(mp3_path, mp3_name).replace(' ', '_').lower()
		src_wav = os.path.join(wav_path, wav_name).replace(' ', '_').lower()
		src_ogg = os.path.join(ogg_path, ogg_name).replace(' ', '_').lower()
		
		sound = AudioSegment.from_file(mp3)
		sound.export(src_mp3, format="mp3")
		sound.export(src_ogg, format="ogg")
		sound = sound.set_channels(1) # set to mono
		sound.export(src_wav, format="wav")


if __name__ == "__main__":
	if not os.path.isdir(root_output):
	    """ Check if OUTPUT_DIR exits """
	    os.mkdir(root_output)

	if not os.path.isdir(mp3_path):
	    """ Check if OUTPUT_DIR exits """
	    os.mkdir(mp3_path)
	
	if not os.path.isdir(wav_path):
	    """ Check if OUTPUT_DIR exits """
	    os.mkdir(wav_path)

	if not os.path.isdir(ogg_path):
	    """ Check if OUTPUT_DIR exits """
	    os.mkdir(ogg_path)

	try:
		main(folder=sys.argv[1])
	except:
		print 'error'
		main()


