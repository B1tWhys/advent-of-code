use crate::common::GridVal;

pub fn solve(grid: &Vec<Vec<GridVal>>) {
    let mut prev_row = grid.first().expect("Input has no lines!").clone();
    let mut split_count = 0;

    for new_row in grid.iter().skip(1) {
        let mut new_row = new_row.clone();
        for i in prev_row.iter().enumerate().filter_map(|(i, val)| {
            if *val == GridVal::Beam {
                Some(i)
            } else { None }
        }) {
            if new_row[i] == GridVal::Splitter {
                assert!(i > 0, "Attempted to split the beam off the left edge of the matrix");
                assert!(i + 1 < new_row.len(), "Attempted to split the beam off the right edge of the matrix");
                split_count += 1;
                new_row[i-1] = GridVal::Beam;
                new_row[i+1] = GridVal::Beam;
            } else {
                new_row[i] = GridVal::Beam;
            }
        }

        prev_row = new_row;
    }

    println!("The beam will be split {split_count} times")
}
