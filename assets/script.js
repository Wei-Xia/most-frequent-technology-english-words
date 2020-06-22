function playWordAudio(w) {
  const word = w.toLowerCase();
  const voiceFileUrl = `http://dict.youdao.com/dictvoice?audio=${word}&type=2`;
  const audio = document.getElementById("voice-file");
  document.getElementById('audioSource').src = voiceFileUrl;
  audio.load();
  audio.play();
  const wordEle = document.getElementById(word);
  wordEle.classList.add('playing');
  setTimeout(() => {
    wordEle.classList.remove('playing');
  }, 1000);
}
