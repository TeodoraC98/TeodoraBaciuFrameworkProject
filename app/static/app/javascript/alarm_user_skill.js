frmJoinEl=document.getElementById("frm_join")
trailDiff=document.getElementById("trail-difficulty").textContent
difficultyLevel=trailDiff.split(" ")
frmJoinEl.addEventListener("submit",(event)=>{
      if(difficultyLevel[1]==='hard'){
        alert("This seems like a difficult one. Please make sure you have all the necessary skills to participate!")
    }
})
