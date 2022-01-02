import os
from tqdm import tqdm
from bs4 import BeautifulSoup
import requests
import genanki
import html
import re
import uuid
import sys

voice_url = 'http://dict.youdao.com/dictvoice?type=2&audio={word}'
PATH = '../_posts'
MEDIA_PATH = 'build'

fy_url = 'http://youdao.com/w/eng/{word}'

def doFy(word):
  wb_data = requests.get(fy_url.format(word=word))
  soup = BeautifulSoup(wb_data.text,'html.parser')
  #print(soup)
  p1 = soup.find('div', class_='baav');
  if hasattr(p1, 'get_text') : 
      p1 = p1.get_text()
      p1 = re.sub("[\s\t]+", ' ', p1)
  else:
     p1 = ""
  #print(p1.strip());
  tc = soup.find('div',class_='trans-container').find('ul')
  if hasattr(tc, 'get_text') : 
      return p1+tc.get_text();
  else:
     return p1;

os.makedirs(MEDIA_PATH, exist_ok=True)
os.chdir(MEDIA_PATH)

deckId = 2059400110
my_deck = genanki.Deck(
  deckId,
  '程序员英语词汇宝典')


style = """
.card {

}
#w {
 font-family: arial;
 font-size: 24px;
 text-align: center;
 color: black;
 background-color: white;
 width:100%;
}

#w {
 cursor:pointer;
}
.eudic,.audio, .mSents {
 z-index: 9999;
 position: fixed;
 margin: 0 auto;
 border-radius: 3px;
 opacity:0.60;
 text-align:right;
 background-color:lightgray;
 font-size:20px;
}

/*悬浮查词按钮*/
.eudic { 
 left:2px;
 top:165px;
 padding:10px;
}
/*发音按钮*/
.audio {
 left:2px;
 bottom:120px;
 width:40px;
 font-size:25px;
}

.mSents {
  bottom:120px;
  right: 3px;
}
#toolbar1 a{ text-decoration: none !important;}
"""

my_model = genanki.Model(
  1091735106,
  'SimpleModel1',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
    {'name': 'MyMedia'},
    {'name': 'fy'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '''<h3 id=w role=w>{{Question}}<h3>
<hr/>
<div id=a1>{{MyMedia}}</div>


<!-- anki 英文单词工具条：支持选中或当前单词即时欧路词典查询/有道朗读/有道例句 -->
<span id=toolbar1>
<div class="eudic">
<a href="javascript:go4eudic()">&#128269</a>
</div>

<div class="audio"><a class="replay-button soundLink" href="#" id=playX1>▶️</a>
</div>
<div class="mSents"><a href="javascript:moreSentsLink()" title="更多">&#128227</a>
</div>

<audio id="dictVoice" style="display: none"></audio>
</span>
<script>
String.prototype.trim = function(){
    return this.replace(/(^\s*)|(\s*$)/g,"");
}

function getSelectedText() {
    if (document.Selection) { //ie浏览器
        return document.selection.createRange().text;
    } else { //标准浏览器
        return window.getSelection().toString();
    }
}

var player = document.getElementById('dictVoice');
var playAudio = function(url) {
    player.setAttribute('src', url);
    player.volume = 1;
    player.play();
}

document.querySelector("#playX1").addEventListener("click", function(event) {
        playX();
   event.preventDefault();
}, false);

function playX(w) {
    if(!w){
        w = getSelectedText();
    }
    if (w){
        var url = "https://dict.youdao.com/dictvoice?audio="+encodeURIComponent(w);
        playAudio(url);
    } else {
       document.querySelector('#a1 a').click();
      //  location.href=encodeURIComponent(document.querySelector('#a1 a').outerHTML);
    }
    return false;
}

//
function go4eudic(w) {
    if(!w){
        w = getSelectedText();
    }
    if (!w){
        w=document.querySelector('#w').innerText.trim()
    }
    var href = "intent:peek#Intent;action=colordict.intent.action.SEARCH;category=android.intent.category.DEFAULT;type=text/plain;component=com.eusoft.eudic/com.eusoft.dict.activity.dict.LightpeekActivity;scheme=eudic;S.EXTRA_QUERY="+w+";end"
    location.href=href;
}

function moreSentsLink(w) {
   if(!w){
        w = getSelectedText();
   } 
   if(!w){
       var w = document.getElementById('w').innerText.trim()
     }
    var url = "https://m.youdao.com/singledict?q="+encodeURIComponent(w) + "&le=eng&dict=blng_sents&more=true"
    location.href = url;
}


var initVoice = function () {
    document.addEventListener('click', function (e) {
        var target = e.target;
        if (target.hasAttribute('role')) {
            var role = target.getAttribute('role');
            if (role == "w"){
                    playX();
            } else if (role == "msents"){
                  moreSentsLink(); 
            } else if (role == "voice"){
               var w= target.parentNode.nextElementSibling.querySelector("p").innerText.trim();
                  playX(w);
            } else if (role.indexOf('dict1') >= 0){
                var w = target.innerText.trim();
                 go4eudic(w)
            } else {
                  return;
            }
            e.preventDefault();
        }
    }, false);
};
initVoice()
</script>

''',
      'afmt': '''{{FrontSide}}
<hr id="answer">
<div id=answer1>{{Answer}}</div>
<hr/>
<div id=fy1>{{fy}}</div>''',
    }
  ], css=style)

my_package = genanki.Package(my_deck)

testOnly = False if len(sys.argv) < 2 else ("testOnly" == sys.argv[1]);
for filename in tqdm(os.listdir(PATH)):
  word = filename.split('-')[-1][:-3]  # eg 2020-01-01-agile.md
  filePath = os.path.join(PATH, filename)
  content = open(filePath, encoding='utf-8').read()
  #print(content)
  fyWord = doFy(word);
  fyWord = html.escape(fyWord);
  fyWord = fyWord.replace('\n','<br/>')
  #print(fyWord)
  #if len(fyWord) > 0:
  #  content=("%s\nfy:\n%s"%(content.strip(),fyWord.strip()))
  #  
  content = re.sub("(?m)^-+", '', content).strip();
  #print(content)
  content = html.escape(content);
  content = content.replace('\n','<br/>')
  voicePath = '{}.mp3'.format(word)
  r = requests.get(voice_url.format(word=word))
  f = open(voicePath,'wb')
  f.write(r.content)
  f.close();
  guid = str(uuid.uuid3(uuid.NAMESPACE_OID, str(deckId) + word));
  my_note = genanki.Note(
    model=my_model,
    fields=[word, content, '[sound:{}]'.format(voicePath), fyWord], guid=guid)
  my_deck.add_note(my_note)
  my_package.media_files.append(voicePath)
  if testOnly:
     break

my_package.write_to_file('most-frequent-technology-english-words.apkg')

for filename in my_package.media_files:
  if os.path.exists(filename):
    os.remove(filename)