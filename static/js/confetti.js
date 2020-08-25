$(document).ready(function() {


    let canvas = document.getElementById('confetti');

    canvas.width = 640;
    canvas.height = 640;
    
    let ctx = canvas.getContext('2d');
    let pieces = [];
    let numberOfPieces = 350;
    let lastUpdateTime = Date.now();
    
    function randomColor () {
        let colors = ['#4ecf55', '#b8ffd4', '#5bab7a', '#91deed', '#7ad61e', '#9dc441'];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    var confettiCount = 0;
    
    function update () {
        let now = Date.now(),
            dt = now - lastUpdateTime;
    
        for (let i = pieces.length - 1; i >= 0; i--) {
            let p = pieces[i];
    
            if (p.y > canvas.height) {
                pieces.splice(i, 1);
                continue;
            }
    
            p.y += p.gravity * dt;
            p.rotation += p.rotationSpeed * dt;
        }
    
        if (confettiCount < 45) {
            if (pieces.length < numberOfPieces) {
                pieces.push(new Piece(Math.random() * canvas.width, -20));
                confettiCount += 1;
            }
        }
      
    
        lastUpdateTime = now;
    
        setTimeout(update, 1);
    }
    
    function draw () {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    
        pieces.forEach(function (p) {
            ctx.save();
    
            ctx.fillStyle = p.color;
    
            ctx.translate(p.x + p.size / 2, p.y + p.size / 2);
            ctx.rotate(p.rotation);
    
            ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
    
            ctx.restore();
        });
    
        requestAnimationFrame(draw);
    }
    
    function Piece (x, y) {
        this.x = x;
        this.y = y;
        if (window.innerWidth < 500) {
            this.size = (Math.random() * 0.1 + 0.75) * 02;
        } else {
            this.size = (Math.random() * 0.1 + 0.75) * 01;
        }
        
        this.gravity = (Math.random() * 0.5 + 0.75) * 0.08;
        this.rotation = (Math.PI * 2) * Math.random();
        this.rotationSpeed = (Math.PI * 2) * (Math.random() - 0.5) * 0.005;
        this.color = randomColor();
    }
    
    while (pieces.length < numberOfPieces) {
        pieces.push(new Piece(Math.random() * canvas.width, Math.random() * canvas.height));
    }
    
    update();
    draw();
});
