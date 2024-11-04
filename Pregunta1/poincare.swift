import Foundation

//Function that calculates the n number of poincare conjecture
func poincare(_ n:Int ) -> Int{
    //Aux variable and count
    //I can't modify n while excuting so i need to use value
    var value = n
    var count = 0

    //Returns an error if n < 1
    if n < 1:
        return -1

    //Loop
    while true{
        //If we found the 1
        if value == 1{
            return count
        //Case even number
        }else if value % 2 == 0{
            value = value/2
            count += 1
        //Case odd number
        }else{
            value = (value * 3) + 1
            count += 1
        }
    }
}

print(poincare(7))