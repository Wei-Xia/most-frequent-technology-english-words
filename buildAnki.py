import os
from tqdm import tqdm
import requests
import genanki


voice_url = 'http://dict.youdao.com/dictvoice?type=2&audio={word}'
PATH = '_posts'
# MEDIA_PATH = 'media'


# os.makedirs(MEDIA_PATH, exist_ok=True)
my_deck = genanki.Deck(
  2059400110,
  '程序员英语词汇宝典')


my_model = genanki.Model(
  1091735104,
  'Simple Model with Media',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'MyMedia'},                                 
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}<br>{{MyMedia}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

my_package = genanki.Package(my_deck)
for filename in tqdm(os.listdir(PATH)):
  word = filename.split('-')[-1][:-3]  # eg 2020-01-01-agile.md
  filePath = os.path.join(PATH, filename)
  content = open(filePath, encoding='utf-8').read()
  content = content.replace('\n','<br/>')
  voicePath = '{}.mp3'.format(word) # os.path.join(MEDIA_PATH, '{}.mp3'.format(word))
  r = requests.get(voice_url.format(word=word))
  open(voicePath,'wb').write(r.content)
  my_note = genanki.Note(
    model=my_model,
    fields=[word, content, '[sound:{}]'.format(voicePath)])
  my_deck.add_note(my_note)
  my_package.media_files.append(voicePath)

my_package.write_to_file('most-frequent-technology-english-words.apkg')

for filename in my_package.media_files:
  os.remove(MEDIA_PATH)