use crate::common::GridVal;

pub fn solve(grid: &Vec<Vec<GridVal>>) {
    let mut prev_row: Vec<GridVal> = grid.first().expect("Input has no lines!").clone();
    let mut timeline_counts = vec![0u64; prev_row.len()];
    prev_row.iter()
        .enumerate()
        .find_map(|(i, val)| if *val == GridVal::Beam { Some(i) } else { None })
        .map(|i| timeline_counts[i] = 1);

    for new_row in grid.iter().skip(1) {
        let mut new_row: Vec<GridVal> = new_row.clone();
        let mut new_timeline_counts = vec![0u64; prev_row.len()];

        for i in prev_row.iter().enumerate().filter_map(|(i, val)| {
            if *val == GridVal::Beam {
                Some(i)
            } else { None }
        }) {
            if new_row[i] == GridVal::Splitter {
                assert!(i > 0, "Attempted to split the beam off the left edge of the matrix");
                assert!(i < new_row.len(), "Attempted to split the beam off the left edge of the matrix");

                new_row[i-1] = GridVal::Beam;
                new_timeline_counts[i-1] += timeline_counts[i];
                new_row[i+1] = GridVal::Beam;
                new_timeline_counts[i+1] += timeline_counts[i];
            } else {
                new_row[i] = GridVal::Beam;
                new_timeline_counts[i] += timeline_counts[i];
            }
        }

        prev_row = new_row;
        timeline_counts = new_timeline_counts;
    }

    let total_timelines: u64 = timeline_counts.iter().sum();
    println!("There will be {total_timelines} timelines!")
}
