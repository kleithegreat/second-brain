# include <iostream>
# include <string>
# include <stdexcept>
# include "Post.h"

using std::string, std::vector;

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
    // TODO: extracts candidate tags based on occurrences of # in the post
    vector<string> tags = {};

    for (int i = 0; i < postText.length(); i++) {
        if (postText.at(i) == '#') {
            string tag = "#";

            for (int j = i; j < postText.length(); j++) {
                if (postText.at(j) == ' ' || postText.at(j) == ',' || postText.at(j) == '.' || postText.at(j) == '?' || postText.at(j) == '!') {
                    break;
                }
                tag += postText.at(j);
            }
            
            for (int k = 0; k < tag.length(); k++) {
                if (tag.at(k) >= 'A' && tag.at(k) <= 'Z') {
                    tag.at(k) = tag.at(k) + 32;
                }
            }

            try {
                Tag newTag(tag);
                for (int l = 0; l < tags.size(); l++) {
                    if (tags.at(l) == tag) {
                        throw exception();
                    }
                }
                tags.push_back(tag);
            } catch (std::invalid_argument& e) {
                continue;
            }
        }
    }
}
