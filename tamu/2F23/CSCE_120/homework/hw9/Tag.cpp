# include <string>
# include <stdexcept>
# include "Tag.h"

using std::string, std::vector;

Tag::Tag(string tagName) : tagName(), tagPosts() {
    if (tagName.length() < 2) {
        throw std::invalid_argument("tag constructor: invalid parameter values");
    }
    if (tagName.at(0) != '#') {
        throw std::invalid_argument("tag constructor: invalid parameter values");
    }

    if (tagName.at(1) < 'a' || tagName.at(1) > 'z') {
        throw std::invalid_argument("tag constructor: invalid parameter values");
    }

    for (unsigned int i = 0; i < tagName.length(); i++) {
        if (tagName.at(i) >= 'A' && tagName.at(i) <= 'Z') {
            throw std::invalid_argument("tag constructor: invalid parameter values");
        }
    }

    if (tagName.at(tagName.length() - 1) == '.' || tagName.at(tagName.length() - 1) == ',' || tagName.at(tagName.length() - 1) == '?' || tagName.at(tagName.length() - 1) == '!') {
        throw std::invalid_argument("tag constructor: invalid parameter values");
    }

    this->tagName = tagName;
}

string Tag::getTagName() {
    return tagName;
}

vector<Post*>& Tag::getTagPosts() {
    return tagPosts;
}

void Tag::addTagPost(Post* post) {
    if (post == nullptr) {
        throw std::invalid_argument("tag addTagPost: invalid parameter values");
    }

    tagPosts.push_back(post);
}
