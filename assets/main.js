var a = new Vue({
  el: '#abc',
  data: {
    nowPlaying: false,
    currentWord: "width"
  },
  methods: {
    playNow: function (word) {
      audio.pause()
      a.currentWord = word
      var newAudio = setTimeout("audio.play()",100)
    }
  }
})

window.onload = function(){
  audio = document.getElementById("voice-file")
}
