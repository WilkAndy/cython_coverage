#include "apple.h"
using namespace std;
namespace mango {
    apple::apple(int key) {
            _key = key;
    };
    int apple::execute()
    {
            return _key*_key;
    };
}
