use std::fs::read_to_string;

const FILE_NAME: &str = "/Users/Skyler/Developer/advent-of-code/2025/02/input";

fn solution1() {
    let data = read_to_string(FILE_NAME).unwrap();
    let mut total = 0;

    for range_s in data.trim().split(",") {
        let (lo, hi) = range_s.split_once("-").unwrap();
        let (lo, hi): (i64, i64) = (lo.parse().unwrap(), hi.parse().unwrap());
        for i in lo..(hi+1) {
            let is = i.to_string();
            if is.len() % 2 != 0 {
                continue;
            }
            let first_half = &is[0..is.len() / 2];
            let second_half = &is[is.len() / 2..is.len()];
            if first_half == second_half {
                total += i;
            }
        }
    }
    println!("Solution 1: {total}");
}

fn is_invalid_2(value: &i64) -> bool {
    let is = value.to_string().into_bytes();
    let mut pat: Vec<u8> = Vec::new();
    for i in 0..(is.len() / 2) {
        pat.push(is[i]);
        if is.len() % pat.len() != 0 { continue };
        
        let is_match = is.chunks_exact(pat.len()).all(|chunk| chunk == pat);
        if is_match {
            return true;
        }
    }
    return false;
}

fn solution2() {
    let data = read_to_string(FILE_NAME).unwrap();
    let mut total: i64 = 0;

    for range_s in data.trim().split(",") {
        let (lo, hi) = range_s.split_once("-").unwrap();
        let (lo, hi): (i64, i64) = (lo.parse().unwrap(), hi.parse().unwrap());
        total += (lo..(hi+1)).into_iter().filter(is_invalid_2).sum::<i64>();
    }
    println!("Solution 2: {total}")
}

fn main() {
    solution1();
    solution2();
}
