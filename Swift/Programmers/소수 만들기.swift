import Foundation

func solution(_ nums:[Int]) -> Int {
    var numsSum: [Int] = []
    for i in 0 ..< nums.count - 2 {
        for j in i+1 ..< nums.count - 1 {
            for k in j+1 ..< nums.count {
                numsSum.append(nums[i]+nums[j]+nums[k])
            }
        }
    }
    return numsSum.filter(isPrime(checkNumber:)).count
}

func isPrime(checkNumber: Int) -> Bool {
    let criterion = Int(Double(checkNumber).squareRoot())
    for i in 2...criterion {
        if checkNumber % i == 0 {
            return false
        }
    }
    return true
}