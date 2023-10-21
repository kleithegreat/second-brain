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

    for (unsigned int i = 0; i < MAX_WIDTH; i++) {
        for (unsigned int j = 0; j < MAX_HEIGHT; j++) {

            double mappedX;
            double mappedY;
            mapCoordinates(H, i, j, mappedX, mappedY);

            bool I2Defined = false;
            Pixel I2_pixel;
            if (mappedX >= 0 && mappedX < width2 && mappedY >= 0 && mappedY < height2) {
                I2_pixel = bilinear_interpolation(image2, width2, height2, mappedX, mappedY);
                I2Defined = true;
            }

            bool I1Defined = false;
            Pixel I1_pixel;
            if (i < width1 && j < height1) {
                I1_pixel = image1[i][j];
                I1Defined = true;
            }

            if (I1Defined && I2Defined) {
                image1[i][j] = {static_cast<short>((I1_pixel.r + I2_pixel.r) / 2),
                                static_cast<short>((I1_pixel.g + I2_pixel.g) / 2),
                                static_cast<short>((I1_pixel.b + I2_pixel.b) / 2)};
            } else if (I1Defined && !I2Defined) {
                image1[i][j] = I1_pixel;
            } else if (I2Defined && !I1Defined) {
                image1[i][j] = I2_pixel;
            } else {
                image1[i][j] = {0, 0, 0};
            }
        }
    }

    width1 = MAX_WIDTH;
    height1 = MAX_HEIGHT;
}
