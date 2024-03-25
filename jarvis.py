import time
from threading import Event, Thread  
import os
import playsound
import ollama


chat_memory = '\n\nCHAT HISTORY:\n'

# talking_library = 'pyttsx3'
talking_library = 'TTS.api'
# talking_library = 'gTTS'
# talking_library = 'os'

# https://ollama.com/library?sort=popular
llm_model = 'zephyr'  # too much moralizing
llm_model = 'llama2-uncensored'  # for talking
# llm_model = 'codellama'  # for coding
# llm_model = 'starcoder'  # maybe for coding co-pilot
# llm_model = 'samantha-mistral'  # Shrink

# curl -fsSL https://ollama.com/install.sh | sh
# ollama run llama2-uncensored

set_laguage = 'en'
# set_langage = 'hu'
# set_laguage = 'sk' 

if talking_library == 'TTS.api':
    from TTS.api import TTS
    
    # TTS().list_models()
    # TTS.list_models()
    
    if set_laguage == 'en':
        # tts = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2', progress_bar=True, gpu=True)  # Model is multi-speaker but no `speaker` is provided
        # tts = TTS(model_name='tts_models/en/blizzard2013/capacitron-t2-c150_v2', progress_bar=True, gpu=True)  # Randotron

        tts = TTS(model_name='tts_models/en/jenny/jenny', progress_bar=True, gpu=True,) # The best
        # tts = TTS(model_name='tts_models/en/ljspeech/overflow', progress_bar=True, gpu=True)
    
        # tts = TTS(model_name='tts_models/en/ljspeech/fast_pitch', progress_bar=True, gpu=True)  
        # tts = TTS(model_name='tts_models/en/multi-dataset/tortoise-v2', progress_bar=True, gpu=True)  # Not enough memory
