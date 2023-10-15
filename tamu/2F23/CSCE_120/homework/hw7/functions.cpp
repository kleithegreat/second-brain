#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include "functions.h"

using namespace std;

void loadCorners(const std::string& filename, Corner imageCorners[MAX_CORNERS], unsigned int& numberOfCorners) {
    std::ifstream infile(filename);
    if (!infile.is_open()) {
        throw std::runtime_error("Failed to open " + filename);
    }

    numberOfCorners = 0;
    unsigned int x, y;

    while (infile >> x >> y) {
        if (numberOfCorners >= MAX_CORNERS) {
            throw std::runtime_error("Too many corners in " + filename);
        }
        imageCorners[numberOfCorners].x = x;
        imageCorners[numberOfCorners].y = y;
        numberOfCorners++;
    }

    infile.close();
}

double errorCalculation(Pixel image1[][MAX_HEIGHT], const unsigned int width1, const unsigned int height1,
                      Corner image1corner,
                      Pixel image2[][MAX_HEIGHT], const unsigned int width2, const unsigned int height2,
                      Corner image2corner) {
    double error = 0;
    const int size = 3;
    
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            int x1 = image1corner.x + i;
            int y1 = image1corner.y + j;
            int x2 = image2corner.x + i;
            int y2 = image2corner.y + j;
            
            if (x1 < 0 || y1 < 0 || x1 >= width1 || y1 >= height1 || x2 < 0 || y2 < 0 || x2 >= width2 || y2 >= height2) {
                return INFINITY;
            }
            
            short rDiff = image1[x1][y1].r - image2[x2][y2].r;
            short gDiff = image1[x1][y1].g - image2[x2][y2].g;
            short bDiff = image1[x1][y1].b - image2[x2][y2].b;

            error += abs(rDiff) + abs(gDiff) + abs(bDiff);
        }
    }

    return error;
}


void matchCorners(CornerPair matchedPairs[MAX_CORNERS], unsigned int &matched_count,
                  Pixel image1[][MAX_HEIGHT], const unsigned int width1, const unsigned int height1,
                  Corner image1corners[], unsigned int image1CornerCount,
                  Pixel image2[][MAX_HEIGHT], const unsigned int width2, const unsigned int height2,
                  Corner image2corners[], unsigned int image2CornerCount){

    // Greedy corner matching goes here

}

void mapCoordinates(const double H[3][3], unsigned int x, unsigned int y,
                    double& mapped_x, double& mapped_y){

    // Mapping function for this week

}

void mergeImages( Pixel image1[][MAX_HEIGHT], unsigned int &width1, unsigned int &height1,
                  Pixel image2[][MAX_HEIGHT], const unsigned int width2, const unsigned int height2,
                  double H[3][3] ){
        
    // Similar to image scaling function from last week with some additional steps.
}
