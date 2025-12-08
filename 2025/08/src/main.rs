use std::path::PathBuf;

use clap::{Parser, Subcommand};

use crate::{solution_1::solution1, solution_2::solution2};

mod solution_1;
mod solution_2;

#[derive(Parser)]
#[command(name="asdf")]
struct AdventOfCode {
    #[command(subcommand)]
    command: Solutions
}

#[derive(Subcommand)]
enum Solutions {
    #[command(name="1")]
    Solution1{ path_buf: PathBuf },
    #[command(name="2")]
    Solution2{ path_buf: PathBuf }
}

fn main() {
    let cli = AdventOfCode::parse();

    match &cli.command {
        Solutions::Solution1{ path_buf } => solution1(&path_buf),
        Solutions::Solution2{ path_buf } => solution2(&path_buf),
    }
}
