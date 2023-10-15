#include <iostream>
#include <sstream>
#include <fstream>
#include <cmath>
#include "functions.h"

using namespace std;

// Copy code from last week for local run. Gradescope will use it's own copy

void loadImage(string filename, Pixel image[][MAX_HEIGHT], unsigned int& width, unsigned int& height) {
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

  for (unsigned int row = 0; row < height; row++) {
    for (unsigned int col = 0; col < width; col++) {
      int r, g, b;
      inFile >> r >> g >> b;

      if (!inFile || r < 0 || r >= 256 || g < 0 || g >= 256 || b < 0 || b >= 256) {
          throw runtime_error("Invalid color value");
      }

      image[col][row] = {static_cast<short>(r), static_cast<short>(g), static_cast<short>(b)};
    }
  }

  int dummy;
  inFile >> dummy;
  if (inFile) {
      throw runtime_error("Too many values");
  }

}

void outputImage(string filename, Pixel image[][MAX_HEIGHT], unsigned int width, unsigned int height) {
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

Pixel bilinear_interpolation(Pixel image[][MAX_HEIGHT], unsigned int width, unsigned int height, double x, double y) {
  int x_floor = static_cast<int>(floor(x));
  int y_floor = static_cast<int>(floor(y));
  int x_ceil = x_floor + 1;
  int y_ceil = y_floor + 1;
  x_floor = max(0, x_floor);
  y_floor = max(0, y_floor);
  x_ceil = min(static_cast<int>(width) - 1, x_ceil);
  y_ceil = min(static_cast<int>(height) - 1, y_ceil);

  Pixel P1 = image[x_floor][y_floor];
  Pixel P2 = image[x_ceil][y_floor];
  Pixel P3 = image[x_floor][y_ceil];
  Pixel P4 = image[x_ceil][y_ceil];

  double dx = x - x_floor;
  double dy = y - y_floor;

  Pixel result;
  result.r = round((1 - dx) * (1 - dy) * P1.r + dx * (1 - dy) * P2.r + (1 - dx) * dy * P3.r + dx * dy * P4.r);
  result.g = round((1 - dx) * (1 - dy) * P1.g + dx * (1 - dy) * P2.g + (1 - dx) * dy * P3.g + dx * dy * P4.g);
  result.b = round((1 - dx) * (1 - dy) * P1.b + dx * (1 - dy) * P2.b + (1 - dx) * dy * P3.b + dx * dy * P4.b);

  return result;
}

double map_coordinates(unsigned int source_dimension, unsigned int target_dimension, unsigned int pixel_coordinate){
  return (static_cast<double>(source_dimension) - 1) / (target_dimension - 1) * pixel_coordinate; 
}

void scale_image(Pixel sourceImage[][MAX_HEIGHT], unsigned int sourceWidth, unsigned int sourceHeight,
                 Pixel targetImage[][MAX_HEIGHT], unsigned int targetWidth, unsigned int targetHeight){
  for (unsigned int row = 0; row < targetHeight; row++) {
    for (unsigned int col = 0; col < targetWidth; col++) {
      
      double source_x = map_coordinates(sourceWidth, targetWidth, col);
      double source_y = map_coordinates(sourceHeight, targetHeight, row);
      
      Pixel color = bilinear_interpolation(sourceImage, sourceWidth, sourceHeight, source_x, source_y);
      
      targetImage[col][row] = color;
    }
  }
}
