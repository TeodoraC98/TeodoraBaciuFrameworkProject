frmJoinEl=document.getElementById("frm_join")
trailDiff=document.getElementById("trail-difficulty").textContent
difficultyLevel=trailDiff.split(" ")
// If a user wants to participate in 
// a route that is marked as difficult, they are informed of the difficulty level of the route.
frmJoinEl.addEventListener("submit",(event)=>{
      if(difficultyLevel[1]==='hard'){
        alert("This seems like a difficult one. Please make sure you have all the necessary skills to participate!")
    }
})

