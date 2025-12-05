use std::{collections::{HashSet, VecDeque}, env::args, fs::read_to_string};

const DELTAS: [(isize, isize); 8] = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)];

struct Neighbors {
    i: usize,
    w: isize,
    h: isize,
    r: usize,
    c: usize
}

impl Neighbors {
    fn new(r: usize, c: usize, w: usize, h: usize) -> Neighbors {
        Neighbors { i: 0, w: w as isize, h: h as isize, r, c }
    }
}

impl Iterator for Neighbors {
    type Item = (usize, usize);

    fn next(&mut self) -> Option<Self::Item> {
        if self.i >= DELTAS.len() {
            return None;
        };


        while self.i < DELTAS.len() {
            let (dr, dc) = DELTAS[self.i];
            let (r, c) = (self.r as isize + dr, self.c as isize + dc);
            self.i += 1;
            if 0 <= r && r < self.h && 0 <= c && c < self.w {
                return Some((r as usize, c as usize));
            }
        }
        return None;
    }
}

fn load_grid() -> Vec<Vec<char>> {
    let path = args().nth(1).unwrap();
    let mut grid = vec![];

    for line in read_to_string(path).unwrap().trim().lines() {
        let mut row = Vec::new();

        for char in line.chars() {
            row.push(char);
        }

        grid.push(row);
    }

    return grid;
}

fn solution_2(grid: &Vec<Vec<char>>) {
    let w = grid[0].len();
    let h = grid.len();

    let mut nbr_counts: Vec<Vec<i32>> = vec![vec![0; w as usize]; h as usize];

    for (r, row) in grid.iter().enumerate() {
        for (c, chr) in row.iter().enumerate() {
            if *chr != '@' { continue };

            for (r, c) in Neighbors::new(r, c, w, h) {
                nbr_counts[r][c] += 1;
            }
        }
    }
    
    let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
    for (r, row) in nbr_counts.iter_mut().enumerate() {
        for (c, count) in row.iter_mut().enumerate() {
            if *count < 4 && grid[r][c] == '@' {
                queue.push_back((r, c));
            }
        }
    }

    let mut removed: HashSet<(usize, usize)> = HashSet::new();
    while let Some((r, c)) = queue.pop_front() {
        if removed.contains(&(r, c)) {continue};

        removed.insert((r, c));
        for (r, c) in Neighbors::new(r, c, w, h).filter(|(r_, c_)| grid[*r_][*c_] == '@') {
            nbr_counts[r][c] -= 1;
            if nbr_counts[r][c] < 4 {
                queue.push_back((r, c))
            }
        }
    }

    let ans = removed.len();
    println!("The answer is: {ans}");
}

fn main() {
    let grid = load_grid();
    solution_2(&grid);
}
