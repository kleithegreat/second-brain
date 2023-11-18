# include <iostream>
# include <string>
# include <stdexcept>
# include <cctype>
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

    for (unsigned int i = 0; i < postText.length(); i++) {
        if (postText[i] == '#') {
            string tag = "#";

            unsigned int j = i + 1;
            for (; j < postText.length(); j++) {
                char currentChar = postText[j];
                if (isspace(currentChar) || currentChar == '#') {
                    break;
                }
                if (isupper(currentChar)) {
                    currentChar = tolower(currentChar);
                }
                tag += currentChar;
            }
            // remove trailing ,.!? on tag if any
            while (tag.length() > 1 && (tag[tag.length() - 1] == ',' || tag[tag.length() - 1] == '.' || tag[tag.length() - 1] == '!' || tag[tag.length() - 1] == '?')) {
                tag = tag.substr(0, tag.length() - 1);
            }
            
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

            i = j;
            }
        }

    return tags;
}

