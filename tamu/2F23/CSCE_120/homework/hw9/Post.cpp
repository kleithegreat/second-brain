# include <iostream>
# include <string>
# include <stdexcept>
# include "Post.h"

using std::string;
using std::vector;

Post::Post(unsigned int postId, string userName, string postText) : postId(postId), userName(userName), postText(postText) {
    if (postId == 0 || userName == "" || postText == "") {
        throw std::invalid_argument("post constructor: invalid parameter values");
    }
}

unsigned int Post::getPostId() {
    return postId;
}

string Post::getPostUser() {
    return userName;
}

string Post::getPostText() {
    return postText;
}

vector<string> Post::findTags() {
    vector<string> tags;

    for (size_t i = 0; i < postText.length(); ++i) {
        if (postText[i] == '#') {
            string tag = "#";

            size_t j = i + 1;
            for (; j < postText.length(); ++j) {
                char currentChar = postText[j];
                if (currentChar == ' ' || currentChar == ',' || currentChar == '.' ||
                    currentChar == '?' || currentChar == '!' || currentChar == '\t' ||
                    currentChar == '\n' || currentChar == '\r') {
                    break;
                }
                if (currentChar >= 'A' && currentChar <= 'Z') {
                    currentChar += 32;
                }
                tag += currentChar;
            }

            if (tag.length() > 1) {
                bool isUnique = true;
                for (const auto& existingTag : tags) {
                    if (existingTag == tag) {
                        isUnique = false;
                        break;
                    }
                }
                if (isUnique) {
                    tags.push_back(tag);
                }
            }

            i = j;
        }
    }

    return tags;
}
