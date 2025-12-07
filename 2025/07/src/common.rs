use std::{fs::read_to_string, path::PathBuf};

use anyhow::{Result, Context};

#[derive(Debug, Clone, PartialEq)]
pub enum GridVal {
    Empty,
    Splitter,
    Beam
}

impl From<char> for GridVal {
    fn from(value: char) -> Self {
        match value {
            '.' => GridVal::Empty,
            '^' => GridVal::Splitter,
            'S' => GridVal::Beam,
            _ => panic!("Unexpected char: `{value}` when converting to GridVal")
        }
    }
}

pub fn read_grid(input_path: &PathBuf) -> Result<Vec<Vec<GridVal>>> {
    let input = read_to_string(input_path)
        .with_context(|| "Error reading input file")?
        .trim()
        .to_string();

    let result = input
        .lines()
        .map(|line| line.chars().map(GridVal::from).collect())
        .collect();
    Ok(result)
}
