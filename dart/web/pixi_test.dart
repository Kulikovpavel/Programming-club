import 'dart:html';
import 'package:pixi/pixi.dart';
import 'keyboard.dart';


void main()
{
    
  
  new Game();
}

class Game
{
  var renderer    = new WebGLRenderer(width: window.innerWidth-100, height: window.innerHeight-100 );
  var stage       = new Stage(new Colour.fromHtml('#6f9'));
  var bunny       = new Sprite.fromImage("images/bunny1.png");
  var prev_time   = 0;
  
  Keyboard keyboard;
  
  Game(){
    document.body.append(this.renderer.view);

    keyboard = new Keyboard();
    
    var assetsToLoader = ["images/texturepack.json"];
    var loader = new AssetLoader(assetsToLoader);
    loader.onComplete.listen((c) => this._onLoaded());
    loader.load();
  }
  
  void _onLoaded(){   
    var bunnyTextures = [new Texture.fromFrame('bunny1.png'), new Texture.fromFrame('bunny2.png'), new Texture.fromFrame('bunny3.png')];
    this.bunny = new MovieClip(bunnyTextures)
              ..animationSpeed = 0.01
              ..gotoAndPlay(0); 
    this.bunny.anchor   = new Point(0.5, 0.5);
    this.bunny.position = new Point(200, 150);
    this.stage.children.add(this.bunny);
    
    window.requestAnimationFrame(this._update); 
  }
  
  void _update(num)
  {
    window.requestAnimationFrame(this._update);
    
    var dt = (num - this.prev_time);
    this.prev_time = num;
    
    handleInput(dt);
    
    //this.bunny.rotation += 0.01*1000*dt;

    this.renderer.render(this.stage);
  }
  
  void handleInput(dynamic dt) {
    var dx=0, dy=0;

    if (keyboard.isPressed(KeyCode.LEFT)) dx += -dt;
    if (keyboard.isPressed(KeyCode.RIGHT)) dx += dt;
    if (keyboard.isPressed(KeyCode.UP)) dy += -dt;
    if (keyboard.isPressed(KeyCode.DOWN)) dy += dt;
    
    if (dx != 0 || dy != 0) this.bunny.position += new Point(dx, dy);
  }
  
  
  
}