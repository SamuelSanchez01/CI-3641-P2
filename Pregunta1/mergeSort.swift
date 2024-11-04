import Foundation

//Function merge, takes 2 sorted array and returns the sorted array of all the elements in both arrays
func merge(left:[Int],right:[Int]) -> [Int] {
    //Aux list to return
    var mergedList = [Int]()
    var left = left
    var right = right
    
    //Merge pseudocode
    while left.count > 0 && right.count > 0 {
        if left.first! < right.first! {
            mergedList.append(left.removeFirst())
        } else {
            mergedList.append(right.removeFirst())
        }
    }

    return mergedList + left + right
}

//Mergesort Algorithm
func mergeSort(_ list:[Int]) -> [Int] {
    //If the list have less than 2 elements returns list
    guard list.count > 1 else {
        return list
    }
    
    //Divide in two parts the list
    let leftList = Array(list[0..<list.count/2])
    let rightList = Array(list[list.count/2..<list.count])
    
    //Apply merge on mergesort of bot lists
    return merge(left: mergeSort(list:leftList), right: mergeSort(list:rightList))
}

let array = [5,10,1,56,3,2,24]

print(mergeSort(array))
