import UIKit

func solution(_ s:String) -> String {
    let array_s = Array(s)
    if array_s.count % 2 == 0 {
        return String(array_s[array_s.count/2-1]) + String(array_s[array_s.count/2])
    } else {
        return String(array_s[array_s.count/2])
    }
}

print(solution("abcde"))



