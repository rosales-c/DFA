# README

DESCRIPTION: Given the size of an integer, this program will find how many numbers from 0-largest integer of size, are
    weakly divisible by 7. Weakly divisible by 7 means that a number is naturally divisible by 7 or if you remove a
    digit it becomes divisible by 7.
    Ex: 141 is not divisible by 7, but removing the last 1 will make it 14 which is weakly divisible by 7.

INPUT: Single numerical input or .txt file with numbers separated by white space. Anything other than digits will be
    ignored.

    LIMITATIONS: There is no limit to the size the program can compute HOWEVER it is limited by the CPU being used. On a
        2018 15" MacBook Pro with Intel Core i7-8750H it took 42 seconds to run a check on a integer of size 100. For
        the purpose of this interview question, I will be limiting the size of the integer to no larger than 20 digits.

OUTPUT: The program will display the size of the digit and the number of integers that are weakly divisible by 7.