import 'dart:html';

class Keyboard {
  Map<int, int> _keys = new Map<int, int>();

  Keyboard() {
    window.onKeyDown.listen((KeyboardEvent e) {
      // If the key is not set yet, set it with a timestamp.
      if (!_keys.containsKey(e.keyCode))
        _keys[e.keyCode] = e.timeStamp;
    });

    window.onKeyUp.listen((KeyboardEvent e) {
      _keys.remove(e.keyCode);
    });
  }

  /**
   * Check if the given key code is pressed. You should use the [KeyCode] class.
   */
  isPressed(int keyCode) => _keys.containsKey(keyCode);
}