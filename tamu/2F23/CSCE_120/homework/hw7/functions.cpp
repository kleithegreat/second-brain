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

    int hood = ERROR_NEIGHBORHOOD_SIZE;
    
    if (static_cast<int>(image1corner.x) - hood/2 < 0 || image1corner.x + hood/2 >= width1 ||
        static_cast<int>(image1corner.y) - hood/2 < 0 || image1corner.y + hood/2 >= height1 ||
        static_cast<int>(image2corner.x) - hood/2 < 0 || image2corner.x + hood/2 >= width2 ||
        static_cast<int>(image2corner.y) - hood/2 < 0 || image2corner.y + hood/2 >= height2) {
        return INFINITY;
    }

    double error = 0;

    for (int i = -hood/2; i <= hood/2; i++) {
        for (int j = -hood/2; j <= hood/2; j++) {
            int dr = image1[image1corner.x + i][image1corner.y + j].r - image2[image2corner.x + i][image2corner.y + j].r;
            int dg = image1[image1corner.x + i][image1corner.y + j].g - image2[image2corner.x + i][image2corner.y + j].g;
            int db = image1[image1corner.x + i][image1corner.y + j].b - image2[image2corner.x + i][image2corner.y + j].b;

            error += abs(dr) + abs(dg) + abs(db);
        }
    }
    return error;
}


void matchCorners(CornerPair matchedPairs[MAX_CORNERS], unsigned int &matched_count,
                  Pixel image1[][MAX_HEIGHT], const unsigned int width1, const unsigned int height1,
                  Corner image1corners[], unsigned int image1CornerCount,
                  Pixel image2[][MAX_HEIGHT], const unsigned int width2, const unsigned int height2,
                  Corner image2corners[], unsigned int image2CornerCount) {
    
    Corner usedCorners[MAX_CORNERS] = {};
    
    for (unsigned int i = 0; i < image1CornerCount; i++) {
        double minError = INFINITY;
        Corner img1min;
        Corner img2min;

        for (unsigned int j = 0; j < image2CornerCount; j++) {
            bool used = false;
            for (unsigned int k = 0; k < matched_count; k++) {
                if (image2corners[j].x == usedCorners[k].x && image2corners[j].y == usedCorners[k].y) {
                    used = true;
                    break;
                }
            }

            if (used) continue;

            double error = errorCalculation(image1, width1, height1, image1corners[i],
                                            image2, width2, height2, image2corners[j]);
            if (error < minError) {
                minError = error;
                img1min = image1corners[i];
                img2min = image2corners[j];
            }
        }

        if (minError < INFINITY){
            matchedPairs[matched_count].image1Corner = img1min;
            matchedPairs[matched_count].image2Corner = img2min;
            matchedPairs[matched_count].error = minError;
            usedCorners[matched_count] = img2min;
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
