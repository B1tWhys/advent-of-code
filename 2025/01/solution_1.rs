use std::fs::read_to_string;

// const FILE_NAME: &'static str = "sample_input";
const FILE_NAME: &'static str = "input";

fn main() {
    let input = read_to_string(FILE_NAME).unwrap();
    let input_lines = input.lines();

    let mut dial = 50;
    let mut ans = 0;
    for line in input_lines {
        println!("line: {}", line);
        let direction = &line[0..1];
        println!("\tdirection: {}", direction);
        let sign = if direction == "R" { 1 } else { -1 };
        println!("\tsign: {}", sign);
        let dist = &line[1..line.len()].parse::<i32>().unwrap() * sign;
        println!("\tdist: {}", dist);
        dial += dist;
        dial %= 100;
        if dial == 0 {
            ans += 1;
        }
        println!("\tdial: {} ans: {ans}", dial);
    }
    println!("\nans: {}", ans);
}
