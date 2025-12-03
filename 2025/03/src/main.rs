use std::{cmp::max, fs::read_to_string};

const N: usize = 12;
const PATH: &str = "/Users/Skyler/Developer/advent-of-code/2025/03/input";

fn max_joltage(bank: &Vec<u8>) -> u64 {
    let mut memo = vec![0 as u64; (N+1) as usize];

    for bank_length in 1..(bank.len()+1) {
        let mut new_memo = Vec::with_capacity(N+1);
        new_memo.push(0);
        for n in 1..(N+1) {
            new_memo.push(max(
                memo[n-1] * 10 + (bank[bank_length-1] as u64),
                memo[n]
            ))
        }
        memo = new_memo;
    }
    return *memo.last().unwrap();
}

fn main() {
    let ans = read_to_string(PATH).unwrap().lines()
        .map(|line| {
            let bank = line.bytes().map(|b| b - b'0').collect();
            return max_joltage(&bank);
        })
        .sum::<u64>();
    println!("Result: {ans}");
}
