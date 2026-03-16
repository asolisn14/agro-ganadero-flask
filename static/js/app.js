// ============================
// PARTICULAS INTERACTIVAS
// ============================

const canvas = document.getElementById("bg-canvas")
const ctx = canvas.getContext("2d")

canvas.width = window.innerWidth
canvas.height = window.innerHeight

let particles = []

class Particle{

constructor(x,y){

this.x = x
this.y = y

this.size = Math.random()*2

this.speedX = Math.random()*1-0.5
this.speedY = Math.random()*1-0.5

}

update(){

this.x += this.speedX
this.y += this.speedY

}

draw(){

ctx.fillStyle = "rgba(255,255,255,0.3)"

ctx.beginPath()

ctx.arc(this.x,this.y,this.size,0,Math.PI*2)

ctx.fill()

}

}

function init(){

particles = []

for(let i=0;i<120;i++){

let x = Math.random()*canvas.width
let y = Math.random()*canvas.height

particles.push(new Particle(x,y))

}

}

function animate(){

ctx.clearRect(0,0,canvas.width,canvas.height)

particles.forEach(p => {

p.update()
p.draw()

})

requestAnimationFrame(animate)

}

init()
animate()

// ============================
// EFECTO MOUSE
// ============================

window.addEventListener("mousemove",e=>{

for(let i=0;i<3;i++){

particles.push(new Particle(e.x,e.y))

}

if(particles.length>200){

particles.splice(0,10)

}

})

window.addEventListener("resize",()=>{

canvas.width = window.innerWidth
canvas.height = window.innerHeight

})