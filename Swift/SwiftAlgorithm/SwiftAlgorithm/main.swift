//
//  main.swift
//  SwiftAlgorithm
//
//  Created by Seungjin Baek on 2021/07/02.
//

import Foundation


// 네이버 웹툰 2021 상반기
//func solution1(_ win_lose:[Int]) -> Int{
//    var maxStraightWin = 0
//    var partialStraightWin = 0
//    for gameResult in win_lose {
//        if (gameResult == 1) {
//            partialStraightWin += 1
//            maxStraightWin = biggerNumber(currentMax: maxStraightWin, candidateMax: partialStraightWin)
//            continue
//        }
//        partialStraightWin = 0
//    }
//    return maxStraightWin
//}
//
//func biggerNumber(currentMax: Int, candidateMax: Int) -> Int {
//    if (currentMax >= candidateMax) {
//        return currentMax
//    }
//    return candidateMax
//}


//func solution(_ n:Int, _ clockwise:Bool) -> [[Int]] {
//    var arrayByGivenN : [[Int]] = Array(repeating: Array(repeating: 0, count: n), count: n)
//
//    return []
//}
//
//func startToMoveRight(startRow: Int, startCol: Int, n: Int, clockwise: Bool) -> [(Int, Int)] {
//    var movePoints: [(Int, Int)] = [(startRow, startCol)]
//    var direction: Int {
//        if (clockwise) { return 1 }
//        else { return -1 }
//    }
//
//
//    return movePoints
//}
//

//
func solution(_ play_list: [Int], _ listen_time: Int) -> Int {
    var songList: [Song] = []
    var timeCriteria: [Int] = [-1, 1]
    var currentTime = 0
    for songLength in play_list {
        songList.append(Song(startTime: currentTime, endTime: currentTime+songLength))
        currentTime += songLength
        timeCriteria += [currentTime-1, currentTime+1]
    }
    
    return 0
}

struct Song {
    let startTime: Int
    let endTime: Int
}
