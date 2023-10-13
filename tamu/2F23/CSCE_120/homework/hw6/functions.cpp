#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include "functions.h"

using namespace std;

void initializeImage(Pixel image[][MAX_HEIGHT]) {
  // iterate through columns
  for (unsigned int col = 0; col < MAX_WIDTH; col++) {
    // iterate through rows
    for (unsigned int row = 0; row < MAX_HEIGHT; row++) {
      // initialize pixel
      image[col][row] = {0, 0, 0};
    }
  }
}

void loadImage(string filename, Pixel image[][MAX_HEIGHT], unsigned int& width, unsigned int& height) {
  // TODO: implement image loading
  ifstream inFile(filename);

  if (!inFile.is_open()) {
      throw runtime_error("Failed to open " + filename);
  }

  string type;
  inFile >> type;
  if (type != "P3" && type != "p3") {
      throw runtime_error("Invalid type " + type);
  }

  inFile >> width >> height;
  if (!inFile || width <= 0 || width > MAX_WIDTH || height <= 0 || height > MAX_HEIGHT) {
      throw runtime_error("Invalid dimensions");
  }

  int maxColor;
  inFile >> maxColor;
  if (maxColor != 255) {
      throw runtime_error("Invalid max color value");
  }

  for (unsigned int col = 0; col < width; col++) {
      for (unsigned int row = 0; row < height; row++) {
          int r, g, b;
          inFile >> r >> g >> b;

          if (!inFile || r < 0 || r >= 256 || g < 0 || g >= 256 || b < 0 || b >= 256) {
              throw runtime_error("Invalid color value");
          }

          image[col][row] = {static_cast<unsigned char>(r), static_cast<unsigned char>(g), static_cast<unsigned char>(b)};
      }
  }

  int dummy;
  inFile >> dummy;
  if (inFile) {
      throw runtime_error("Too many values");
  }

}


void outputImage(string filename, Pixel image[][MAX_HEIGHT], unsigned int width, unsigned int height) {
  // TODO: implement writing image to file
  ofstream outFile(filename);

  if (!outFile.is_open()) {
      throw invalid_argument("Failed to open " + filename);
  }

  outFile << "P3\n";
  outFile << width << " " << height << "\n";
  outFile << "255\n";

  for (unsigned int row = 0; row < height; row++) {
      for (unsigned int col = 0; col < width; col++) {
          outFile << static_cast<int>(image[col][row].r) << " "
                  << static_cast<int>(image[col][row].g) << " "
                  << static_cast<int>(image[col][row].b) << "\n";
      }
  }

}

double map_coordinates(unsigned int source_dimension, unsigned int target_dimension, unsigned int pixel_coordinate){
  // TODO: implement mapping function.
  return (static_cast<double>(source_dimension) - 1) / (target_dimension - 1) * pixel_coordinate; 
}

Pixel bilinear_interpolation(Pixel image[][MAX_HEIGHT], unsigned int width, unsigned int height, double x, double y) {
  // TODO: Implement bilinear interpolation
  int x_floor = (int) floor(x);
  int y_floor = (int) floor(y);
  int x_ceil = (int) ceil(x);
  int y_ceil = (int) ceil(y);

  // Boundary conditions
  if (x_floor < 0) x_floor = 0;
  if (y_floor < 0) y_floor = 0;
  if (x_ceil >= width) x_ceil = width - 1;
  if (y_ceil >= height) y_ceil = height - 1;

  // Get the nearest four pixels
  Pixel P1 = image[y_floor][x_floor];
  Pixel P2 = image[y_floor][x_ceil];
  Pixel P3 = image[y_ceil][x_floor];
  Pixel P4 = image[y_ceil][x_ceil];

  // Interpolate colors for each RGB component
  int red_I1 = (x - x_floor) * P2.r + (x_ceil - x) * P1.r;
  int red_I2 = (x - x_floor) * P4.r + (x_ceil - x) * P3.r;
  int r = (y_ceil - y) * red_I1 + (y - y_floor) * red_I2;

  int green_I1 = (x - x_floor) * P2.g + (x_ceil - x) * P1.g;
  int green_I2 = (x - x_floor) * P4.g + (x_ceil - x) * P3.g;
  int g = (y_ceil - y) * green_I1 + (y - y_floor) * green_I2;

  int blue_I1 = (x - x_floor) * P2.b + (x_ceil - x) * P1.b;
  int blue_I2 = (x - x_floor) * P4.b + (x_ceil - x) * P3.b;
  int b = (y_ceil - y) * blue_I1 + (y - y_floor) * blue_I2;

  // Round the result to get the final color
  Pixel result;
  result.r = round(r);
  result.g = round(g);
  result.b = round(b);

  return result;

}

void scale_image(Pixel sourceImage[][MAX_HEIGHT], unsigned int sourceWidth, unsigned int sourceHeight,
                   Pixel targetImage[][MAX_HEIGHT], unsigned int targetWidth, unsigned int targetHeight){
  // TODO: add loops to calculate scaled images

}