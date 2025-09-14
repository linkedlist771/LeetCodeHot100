#include<algorithm>
#include<vector>

using namespace std;


class MedianFinder {
public:
    vector<int> array;

    MedianFinder() {
        array.clear();   // 初始化为空
    }

    void addNum(int num) {
        array.push_back(num);
    }

    double findMedian() {
        sort(array.begin(), array.end());

        int length = array.size();

        if( length % 2 == 0)
        {
            return (array[length/2-1] + array[length/2])/2.0;
        }
        else
        {
            return  array[(length-1)/2];
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */