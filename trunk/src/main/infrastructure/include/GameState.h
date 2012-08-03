#pragma once
#ifndef GAMESTATE_H_
#define GAMESTATE_H_

enum GameState {
	INITIAL=-1,	// initial state
	GAMEOVER=0,
	MAINMENU,	// in a menu
	PLAYING,
	BRIEFING,
	EDITING,
	OPTIONS,
	NEXTCONQUEST,
	SELECTHOUSE=8,
	INTRO,
	HOUSEINTRODUCTION,
	WINNING,
	WINBRIEF,
	LOSEBRIEF,
	LOSING,
	MISSIONSCORE,
	SETUPSKIRMISH,
};

#endif