var canvas = document.createElement("canvas");  // создаем html-элемент canvas
var ctx = canvas.getContext("2d");  // получаем контекст для рисования
canvas.width = 800;  // устанавливаем размеры
canvas.height = 600;
canvas.style.cssText='margin-left: auto; margin-right: auto; display: block;';  // ставим холст по центру экрана
document.body.appendChild(canvas);  // добавляем холст на экран

ctx.fillStyle = '#06166F';  // цвет заполнения по умолчанию
ctx.fillRect(0, 0, canvas.width, canvas.height);  //заполняем холст фоном
document.addEventListener('keydown', keyDown);  // добавляем вызов функции на событие нажатия кнопки
document.addEventListener('keyup', keyUp);  // функция при отпускании кнопки
 
var isLeftPressed = false;  // переменная для сохранения статуса нажатия кнопки влево
var isRightPressed = false;  // то же самое - для кнопки вправо
 
function keyDown(e) {
	var keyCode = e.keyCode;
	if (keyCode == 37){
		isLeftPressed = true;
	};
	if (keyCode == 39){
		isRightPressed = true;
	};
};
 
function keyUp(e) {
	var keyCode = e.keyCode;
	if (keyCode == 37){
		isLeftPressed = false;
	};
	if (keyCode == 39){
		isRightPressed = false;
	};
};


var player_image = new Image();  
player_image.onload = main;
player_image.src = 'images/bunny.png';

// Game state
var player = {
	speed: 500,  // скорость перемещения
    pos: [canvas.width/2, canvas.height - 50],  // позиция игрока на экране
    half_size: [26/2, 37/2],  // полуразмеры игрока, чтобы отрисовывать в правильном месте
    sprite: player_image
}; 


var enemies = [];

var enemy = {
	speed: 250,
	pos: [Math.random()*canvas.width, 0],
	half_size: [26/2, 37/2],
	sprite: player_image
}

 
 
// The main game loop
var lastTime = 0;

var score = 0;

function main() {
    var now = Date.now();
    var dt = (now - lastTime) / 1000.0;  // дельта времени с последнего прохода функции
	//console.log(dt);
	var is_next_enemy = Math.random() > 0.99
	if (is_next_enemy){
		var enemy = {
		speed: 250,
		pos: [Math.random()*canvas.width, 0],
		half_size: [26/2, 37/2],
		sprite: player_image
		};
		enemies.push(enemy);
	}

	update_player(dt);  // обновляем координаты игрока согласно нажатым клавишам
	update_enemies(dt);
	render();  // перерисовываем экран


	check_collisions();

	// score += 0.017;

    lastTime = now;
    //console.log(Math.random())
    requestAnimationFrame(main);  // цикл анимации
}

function render() {
	ctx.fillStyle = '#06166F';
	ctx.fillRect(0, 0, canvas.width, canvas.height);  //заполняем холст фоном
	ctx.drawImage(player.sprite, player.pos[0]-player.half_size[0], player.pos[1]-player.half_size[1])  // рисуем игрока
	
	var enemies_len = enemies.length;
	for (var i=0; i < enemies_len; i ++){
		var enemy = enemies[i]
		ctx.drawImage(enemy.sprite, enemy.pos[0]-enemy.half_size[0], enemy.pos[1]-enemy.half_size[1])  // рисуем врага
	}	
	ctx.fillStyle = '#FFFFFF';  
	ctx.fillText(Math.floor(score), 10, 10);
}

function update_enemies(dt) {
	var enemies_len = enemies.length;
	for (var i=0; i < enemies_len; i ++){
		var enemy = enemies[i]
		enemy.pos[1] += 0.017*enemy.speed
		console.log(enemy.pos[0]);
		if (enemy.pos[1] > canvas.height) {
		enemy.pos[0] = Math.random()*canvas.width
		enemy.pos[1] = 0
	}
}	

	
}

function update_player(dt) {
	if (isLeftPressed) {player.pos[0] -= dt*player.speed};

	if (isRightPressed) {player.pos[0] += dt*player.speed};


	if (player.pos[0] < player.half_size[0]) {
		player.pos[0] = player.half_size[0]
	};
	if (player.pos[0] > canvas.width - player.half_size[0]) {player.pos[0] = canvas.width - player.half_size[0]};
}

function check_collisions(){
	var enemies_len = enemies.length;
	var new_enemies = []
	for (var i=0; i < enemies_len; i ++){
		var enemy = enemies[i]
		var x_check = !((enemy.pos[0]+enemy.half_size[0] <  player.pos[0]-player.half_size[0] ) ||
			 (enemy.pos[0]-enemy.half_size[0] >  player.pos[0]+player.half_size[0]))

		var y_check = !((enemy.pos[1]+enemy.half_size[1] <  player.pos[1]-player.half_size[1] ) ||
			 (enemy.pos[1]-enemy.half_size[1] >  player.pos[1]+player.half_size[1]))
		
		if (x_check && y_check){
			enemy.speed = 0
			score += 10
		} 	
		else {
			new_enemies.push(enemy)
		}
	}
	enemies = new_enemies;
}
