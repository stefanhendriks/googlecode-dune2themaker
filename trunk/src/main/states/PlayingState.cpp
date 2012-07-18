#include "PlayingState.h"

void PlayingState::draw() {
	//screen->draw(map->getBitmap(), 0, 0);
	viewPort->draw(screen, viewPortX, viewPortY);
	screen->draw(mouse->getBitmap(), mouse->getX(), mouse->getY());
}

void PlayingState::update() {
	mouse->updateState();


	// manipuleer camera/map
// 	if (key[KEY_LEFT]) {
// 		viewPortX--;
// 	}
// 	if (key[KEY_RIGHT]) {
// 		viewPortX++;
// 	}
// 	if (key[KEY_UP]) {
// 		viewPortY--;
// 	}
// 	if (key[KEY_DOWN]) {
// 		viewPortY++;
// 	}

	viewPortX = mouse->getX() - (viewPort->getWidth() / 2);
	viewPortY = mouse->getY() - (viewPort->getHeight() / 2);


	if (key[KEY_ESC]) {
		this->flagToQuitGame();
	}
}


