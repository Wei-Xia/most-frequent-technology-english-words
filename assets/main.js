var a = new Vue({
  el: '#abc',
  data: {
    nowPlaying: false,
    currentWord: "anyway"
  },
  methods: {
    playNow: function (word) {
      if ( word == a.currentWord) {
        audio.pause()
        a.nowPlaying = false;
        console.log('paused');
      }
      else {
        a.nowPlaying = true
        a.currentWord = word
        var newAudio = setTimeout("audio.play()",50)
        console.log(a.nowPlaying);
      }

    }
  }
})

window.onload = function(){
  audio = document.getElementById("voice-file")
}
