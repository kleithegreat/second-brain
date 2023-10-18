#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include "functions.h"

using namespace std;

void loadCorners(const std::string filename, Corner imageCorners[MAX_CORNERS], unsigned int& numberOfCorners) {
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

    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            int x1 = image1corner.x + i;
            int y1 = image1corner.y + j;
            int x2 = image2corner.x + i;
            int y2 = image2corner.y + j;

            if (x1 < 0 || y1 < 0 || x1 >= static_cast<int>(width1) || y1 >= static_cast<int>(height1) ||
                x2 < 0 || y2 < 0 || x2 >= static_cast<int>(width2) || y2 >= static_cast<int>(height2)) {
                return INFINITY;
            }

            error += abs(image1[x1][y1].r - image2[x2][y2].r);
            error += abs(image1[x1][y1].g - image2[x2][y2].g);
            error += abs(image1[x1][y1].b - image2[x2][y2].b);
        }
    }

    return error;
}


void matchCorners(CornerPair matchedPairs[MAX_CORNERS], unsigned int &matched_count,
                  Pixel image1[][MAX_HEIGHT], const unsigned int width1, const unsigned int height1,
                  Corner image1corners[], unsigned int image1CornerCount,
                  Pixel image2[][MAX_HEIGHT], const unsigned int width2, const unsigned int height2,
                  Corner image2corners[], unsigned int image2CornerCount) {

    struct PossibleMatch {
        double error;
        unsigned int image1Index;
        unsigned int image2Index;
    };

    PossibleMatch allMatches[MAX_CORNERS * MAX_CORNERS];
    unsigned int allMatchesCount = 0;

    for (unsigned int i = 0; i < image1CornerCount; i++) {
        for (unsigned int j = 0; j < image2CornerCount; j++) {
            double currentError = errorCalculation(image1, width1, height1, image1corners[i],
                                                   image2, width2, height2, image2corners[j]);
            allMatches[allMatchesCount] = {currentError, i, j};
            allMatchesCount++;
        }
    }

    for (unsigned int i = 0; i < allMatchesCount - 1; i++) {
        for (unsigned int j = 0; j < allMatchesCount - 1 - i; j++) {
            if (allMatches[j].error > allMatches[j + 1].error) {
                PossibleMatch temp = allMatches[j];
                allMatches[j] = allMatches[j + 1];
                allMatches[j + 1] = temp;
            }
        }
    }

    bool image1CornerMatched[MAX_CORNERS] = {false};
    bool image2CornerMatched[MAX_CORNERS] = {false};

    matched_count = 0;

    for (unsigned int i = 0; i < allMatchesCount && matched_count < MAX_CORNERS; i++) {
        if (!image1CornerMatched[allMatches[i].image1Index] && !image2CornerMatched[allMatches[i].image2Index]) {
            matchedPairs[matched_count].image1Corner = image1corners[allMatches[i].image1Index];
            matchedPairs[matched_count].image2Corner = image2corners[allMatches[i].image2Index];
            matchedPairs[matched_count].error = allMatches[i].error;
            
            image1CornerMatched[allMatches[i].image1Index] = true;
            image2CornerMatched[allMatches[i].image2Index] = true;
            
            matched_count++;
        }
    }
}


void mapCoordinates(const double H[3][3], unsigned int x, unsigned int y,
                    double& mapped_x, double& mapped_y) {

    double x_prime = H[0][0]*x + H[0][1]*y + H[0][2];
    double y_prime = H[1][0]*x + H[1][1]*y + H[1][2];
    double z_prime = H[2][0]*x + H[2][1]*y + H[2][2];

    mapped_x = x_prime / z_prime;
    mapped_y = y_prime / z_prime;
}


void mergeImages(Pixel image1[][MAX_HEIGHT], unsigned int &width1, unsigned int &height1,
                 Pixel image2[][MAX_HEIGHT], const unsigned int width2, const unsigned int height2,
                 double H[3][3]) {
    Pixel tempImage[MAX_WIDTH][MAX_HEIGHT] = {};

    for (unsigned int col = 0; col < width1; col++) {
        for (unsigned int row = 0; row < height1; row++) {
            
            double w = H[2][0] * col + H[2][1] * row + H[2][2];
            double mappedX = (H[0][0] * col + H[0][1] * row + H[0][2]) / w;
            double mappedY = (H[1][0] * col + H[1][1] * row + H[1][2]) / w;

            if (mappedX >= 0 && mappedX < width2 && mappedY >= 0 && mappedY < height2) {
                Pixel I2_pixel = bilinear_interpolation(image2, width2, height2, mappedX, mappedY);
                Pixel I1_pixel = image1[col][row];

                Pixel mergedPixel;
                mergedPixel.r = (I1_pixel.r + I2_pixel.r) / 2;
                mergedPixel.g = (I1_pixel.g + I2_pixel.g) / 2;
                mergedPixel.b = (I1_pixel.b + I2_pixel.b) / 2;

                tempImage[col][row] = mergedPixel;
            } else {
                tempImage[col][row] = image1[col][row];
            }
        }
    }

    for (unsigned int col = 0; col < width1; col++) {
        for (unsigned int row = 0; row < height1; row++) {
            image1[col][row] = tempImage[col][row];
        }
    }

    width1 = MAX_WIDTH;
    height1 = MAX_HEIGHT;
}
