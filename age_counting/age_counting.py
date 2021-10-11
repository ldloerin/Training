import requests
import numpy as np
import pandas as pd

r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
challenge_token = 'u4m8p7fb'


age_dict = r.json()['data']
age_list = age_dict.split(',')

def count_matching_ages():
  counter = 0
  for i in range(9, len(age_list), 2):
    age = int(age_list[i].split('=')[1])
    if age >= 50:
      counter += 1
  return counter

def build_output_string(counter, challenge_token):
  challenge_token = str(counter) + challenge_token
  output = ''
  multiples_4 = [n for n in range(1, 1001) if n % 4 == 0]
  for i in range(0, len(challenge_token)):
    if i+1 in multiples_4:
      letter = '_'
    else:
      letter = challenge_token[i]
    output += letter
  return output

counter = count_matching_ages()
output_value = build_output_string(counter, challenge_token)
print(output_value)
