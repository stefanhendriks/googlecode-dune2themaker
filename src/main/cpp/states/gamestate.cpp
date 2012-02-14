#include "gamestate.h"

int GameState::init() {
	// pure virtual
	return 0;
}

void GameState::handleEvents() {
	// pure virtual
}

void GameState::update() {
	// pure virtual
}

void GameState::render() {
	// pure virtual
}

void GameState::onEvent(SDL_Event * event) {
	// pure virtual
}

void GameState::shutdown() {
	//  pure virtual
}