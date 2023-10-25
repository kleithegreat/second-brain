#include <iostream>
#include <fstream>
#include <string>
#include "logic.h"

using std::cout;
using std::endl;
using std::ifstream;
using std::string;

/**
 * TODO: Student implement this function
 * Load representation of the dungeon level from file into the 2D map.
 * Calls createMap to allocate the 2D array.
 * @param   fileName    File name of dungeon level.
 * @param   maxRow      Number of rows in the dungeon table (aka height).
 * @param   maxCol      Number of columns in the dungeon table (aka width).
 * @param   player      Player object by reference to set starting position.
 * @return  pointer to 2D dynamic array representation of dungeon map with player's location., or nullptr if loading fails for any reason
 * @updates  maxRow, maxCol, player
 */
char** loadLevel(const string& fileName, int& maxRow, int& maxCol, Player& player) {
    ifstream file(fileName);
    
    if (!file.is_open()) {
        return nullptr;
    }

    file >> maxRow >> maxCol;
    if(!file) return nullptr;

    file >> player.row >> player.col;
    if(!file) return nullptr;

    if (maxRow <= 0 || maxCol <= 0 || maxRow > 999999 || maxCol > 999999 || player.row < 0 || player.col < 0 || player.row >= maxRow || player.col >= maxCol) {
        return nullptr;
    }

    char** map = createMap(maxRow, maxCol);

    auto isValidTile = [](char tile) {
        return tile == TILE_OPEN || tile == TILE_TREASURE || tile == TILE_AMULET || 
               tile == TILE_MONSTER || tile == TILE_PILLAR || tile == TILE_DOOR || 
               tile == TILE_EXIT;
    };

    for (int i = 0; i < maxRow; i++) {
        for (int j = 0; j < maxCol; j++) {
            if (file.eof()) {
                deleteMap(map, maxRow);
                return nullptr;
            }

            file >> map[i][j];

            if (!isValidTile(map[i][j])) {
                deleteMap(map, maxRow);
                return nullptr;
            }
        }
    }

    string remainingData;
    getline(file, remainingData);

    while (getline(file, remainingData)) {
        for (char ch : remainingData) {
            if (!isspace(ch)) {
                deleteMap(map, maxRow);
                return nullptr;
            }
        }
    }

    map[player.row][player.col] = TILE_PLAYER;

    file.close();
    return map;
}


/**
 * TODO: Student implement this function
 * Translate the character direction input by the user into row or column change.
 * That is, updates the nextRow or nextCol according to the player's movement direction.
 * @param   input       Character input by the user which translates to a direction.
 * @param   nextRow     Player's next row on the dungeon map (up/down).
 * @param   nextCol     Player's next column on dungeon map (left/right).
 * @updates  nextRow, nextCol
 */
void getDirection(char input, int& nextRow, int& nextCol) {
    switch (input) {
        case MOVE_UP:
            nextRow -= 1;
            break;
        case MOVE_DOWN:
            nextRow += 1;
            break;
        case MOVE_LEFT:
            nextCol -= 1;
            break;
        case MOVE_RIGHT:
            nextCol += 1;
            break;
        default:
            break;
    }
}

/**
 * TODO: [suggested] Student implement this function
 * Allocate the 2D map array.
 * Initialize each cell to TILE_OPEN.
 * @param   maxRow      Number of rows in the dungeon table (aka height).
 * @param   maxCol      Number of columns in the dungeon table (aka width).
 * @return  2D map array for the dungeon level, holds char type.
 */
char** createMap(int maxRow, int maxCol) {
    if (maxRow <= 0 || maxCol <= 0) {
        return nullptr;
    }
    char **map = new char*[maxRow];

    for (int i = 0; i < maxRow; i++) {
        map[i] = new char[maxCol];
    }

    for (int i = 0; i < maxRow; i++) {
        for (int j = 0; j < maxCol; j++) {
            map[i][j] = TILE_OPEN;
        }
    }

    return map;
}

/**
 * TODO: Student implement this function
 * Deallocates the 2D map array.
 * @param   map         Dungeon map.
 * @param   maxRow      Number of rows in the dungeon table (aka height).
 * @return None
 * @update map, maxRow
 */
void deleteMap(char**& map, int& maxRow) {
    int temp = maxRow;
    maxRow = 0;

    if (map == nullptr) {
        return;
    }

    for (int i = 0; i < temp; i++) {
        delete[] map[i];
    }

    delete[] map;
    map = nullptr;
}

/**
 * TODO: Student implement this function
 * Resize the 2D map by doubling both dimensions.
 * Copy the current map contents to the right, diagonal down, and below.
 * Do not duplicate the player, and remember to avoid memory leaks!
 * You can use the STATUS constants defined in logic.h to help!
 * @param   map         Dungeon map.
 * @param   maxRow      Number of rows in the dungeon table (aka height), to be doubled.
 * @param   maxCol      Number of columns in the dungeon table (aka width), to be doubled.
 * @return  pointer to a dynamically-allocated 2D array (map) that has twice as many columns and rows in size.
 * @update maxRow, maxCol
 */
char** resizeMap(char** map, int& maxRow, int& maxCol) {
    if (maxRow <= 0 || maxCol <= 0 || maxRow > 999999 || maxCol > 999999 || map == nullptr) {
        return nullptr;
    }
    
    int newMaxRow = 2 * maxRow;
    int newMaxCol = 2 * maxCol;
    
    char** newMap = new char*[newMaxRow];
    for (int i = 0; i < newMaxRow; i++) {
        newMap[i] = new char[newMaxCol];
    }

    for (int i = 0; i < maxRow; i++) {
        for (int j = 0; j < maxCol; j++) {
            newMap[i][j] = map[i][j];
        }
    }

    for (int i = 0; i < maxRow; i++) {
        for (int j = maxCol; j < newMaxCol; j++) {
            if (map[i][j - maxCol] == TILE_PLAYER) {
                newMap[i][j] = TILE_OPEN;
                continue;
            }
            newMap[i][j] = map[i][j - maxCol];
        }
    }

    for (int i = maxRow; i < newMaxRow; i++) {
        for (int j = 0; j < maxCol; j++) {
            if (map[i - maxRow][j] == TILE_PLAYER) {
                newMap[i][j] = TILE_OPEN;
                continue;
            }
            newMap[i][j] = map[i - maxRow][j];
        }
    }

    for (int i = maxRow; i < newMaxRow; i++) {
        for (int j = maxCol; j < newMaxCol; j++) {
            if (map[i - maxRow][j - maxCol] == TILE_PLAYER) {
                newMap[i][j] = TILE_OPEN;
                continue;
            }
            newMap[i][j] = map[i - maxRow][j - maxCol];
        }
    }
    
    for (int i = 0; i < maxRow; i++) {
        delete[] map[i];
    }
    delete[] map;
    
    maxRow *= 2;
    maxCol *= 2;
    
    return newMap;
}

/**
 * TODO: Student implement this function
 * Checks if the player can move in the specified direction and performs the move if so.
 * Cannot move out of bounds or onto TILE_PILLAR or TILE_MONSTER.
 * Cannot move onto TILE_EXIT without at least one treasure. 
 * If TILE_TREASURE, increment treasure by 1.
 * Remember to update the map tile that the player moves onto and return the appropriate status.
 * You can use the STATUS constants defined in logic.h to help!
 * @param   map         Dungeon map.
 * @param   maxRow      Number of rows in the dungeon table (aka height).
 * @param   maxCol      Number of columns in the dungeon table (aka width).
 * @param   player      Player object to by reference to see current location.
 * @param   nextRow     Player's next row on the dungeon map (up/down).
 * @param   nextCol     Player's next column on dungeon map (left/right).
 * @return  Player's movement status after updating player's position.
 * @update map contents, player
 */
int doPlayerMove(char** map, int maxRow, int maxCol, Player& player, int nextRow, int nextCol) {
    auto updatePlayerPosition = [&]() {
        map[player.row][player.col] = TILE_OPEN;
        player.row = nextRow;
        player.col = nextCol;
        map[player.row][player.col] = TILE_PLAYER;
    };
    
    if (nextRow < 0 || nextRow >= maxRow || nextCol < 0 || nextCol >= maxCol) {
        return STATUS_STAY;
    }

    switch (map[nextRow][nextCol]) {
        case TILE_PILLAR:
        case TILE_MONSTER:
            return STATUS_STAY;
        case TILE_TREASURE:
            player.treasure++;
            updatePlayerPosition();
            return STATUS_TREASURE;
        case TILE_AMULET:
            updatePlayerPosition();
            return STATUS_AMULET;
        case TILE_DOOR:
            updatePlayerPosition();
            return STATUS_LEAVE;
        case TILE_EXIT:
            if (player.treasure > 0) {
                updatePlayerPosition();
                return STATUS_ESCAPE;
            } else {
                return STATUS_STAY;
            }
        default:
            updatePlayerPosition();
            return STATUS_MOVE;
    }    
}

/**
 * TODO: Student implement this function
 * Update monster locations:
 * We check up, down, left, right from the current player position.
 * If we see an obstacle, there is no line of sight in that direction, and the monster does not move.
 * If we see a monster before an obstacle, the monster moves one tile toward the player.
 * We should update the map as the monster moves.
 * At the end, we check if a monster has moved onto the player's tile.
 * @param   map         Dungeon map.
 * @param   maxRow      Number of rows in the dungeon table (aka height).
 * @param   maxCol      Number of columns in the dungeon table (aka width).
 * @param   player      Player object by reference for current location.
 * @return  Boolean value indicating player status: true if monster reaches the player, false if not.
 * @update map contents
 */
bool doMonsterAttack(char** map, int maxRow, int maxCol, const Player& player) {
    for (int i = player.row - 1; i >= 0; i--) {
        if (map[i][player.col] == TILE_PILLAR) {
            break;
        }
        if (map[i][player.col] == TILE_MONSTER) {
            map[i][player.col] = TILE_OPEN;
            map[i + 1][player.col] = TILE_MONSTER;
        }
    }
    for (int i = player.row + 1; i < maxRow; i++) {
        if (map[i][player.col] == TILE_PILLAR) {
            break;
        }
        if (map[i][player.col] == TILE_MONSTER) {
            map[i][player.col] = TILE_OPEN;
            map[i - 1][player.col] = TILE_MONSTER;
        }
    }
    for (int i = player.col - 1; i >= 0; i--) {
        if (map[player.row][i] == TILE_PILLAR) {
            break;
        }
        if (map[player.row][i] == TILE_MONSTER) {
            map[player.row][i] = TILE_OPEN;
            map[player.row][i + 1] = TILE_MONSTER;
        }
    }
    for (int i = player.col + 1; i < maxCol; i++) {
        if (map[player.row][i] == TILE_PILLAR) {
            break;
        }
        if (map[player.row][i] == TILE_MONSTER) {
            map[player.row][i] = TILE_OPEN;
            map[player.row][i - 1] = TILE_MONSTER;
        }
    }

    if (map[player.row][player.col] == TILE_MONSTER) {
        return true;
    } else {
        return false;
    }
}
