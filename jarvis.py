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
