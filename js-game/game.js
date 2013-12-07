var canvas = document.createElement("canvas");  // создаем html-элемент canvas
var ctx = canvas.getContext("2d");  // получаем контекст для рисования
canvas.width = 800;  // устанавливаем размеры
canvas.height = 600;
canvas.style.cssText='margin-left: auto; margin-right: auto; display: block;';  // ставим холст по центру экрана
document.body.appendChild(canvas);  // добавляем холст на экран

ctx.fillStyle = '#8CA170';  // цвет заполнения по умолчанию

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


var player_image = new Image(onload=main);  
player_image.onload = main;
player_image.src = 'images/bunny.png';

// Game state
var player = {
    speed: 500,  // скорость перемещения
    pos: [canvas.width/2, canvas.height-50],  // позиция игрока на экране
    half_size: [26/2, 37/2],  // полуразмеры игрока, чтобы отрисовывать в правильном месте
    sprite: player_image
}; 
 
// The main game loop
var lastTime = 0;
function main() {
    var now = Date.now();
    var dt = (now - lastTime) / 1000.0;  // дельта времени с последнего прохода функции
	
	update_player(dt);  // обновляем координаты игрока согласно нажатым клавишам
	render();  // перерисовываем экран

    lastTime = now;
    requestAnimationFrame(main);  // цикл анимации
}

function render() {
	ctx.fillRect(0, 0, canvas.width, canvas.height);  //заполняем холст фоном
	ctx.drawImage(player.sprite, player.pos[0]-player.half_size[0], player.pos[1]-player.half_size[1])  // рисуем игрока
}

function update_player(dt) {
	if (isLeftPressed) {player.pos[0] -= dt*player.speed};
	if (isRightPressed) {player.pos[0] += dt*player.speed};
}
