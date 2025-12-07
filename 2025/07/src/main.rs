mod solution_1;
mod solution_2;
mod common;

use std::path::PathBuf;

use clap::{Parser, Subcommand, Args};
use anyhow::{Result};

use crate::common::read_grid;

#[derive(Parser)]
#[command(name="Advent of code 2025 day 7", version="1.0")]
struct Cli {
    #[command(subcommand)]
    command: Solutions,
}

#[derive(Subcommand)]
enum Solutions {
    /// Solve part 1
    #[command(name="1")]
    Solution1(SolutionArgs),
    #[command(name="2")]
    Solution2(SolutionArgs)
}

#[derive(Args)]
struct SolutionArgs {
    /// Path to the input file
    input_path: PathBuf
}

fn main() -> Result<()> {
    let cli = Cli::parse();

    match &cli.command {
        Solutions::Solution1(args) => {
            let grid = read_grid(&args.input_path)?;
            solution_1::solve(&grid);
        }
        Solutions::Solution2(args) => {
            let grid = read_grid(&args.input_path)?;
            solution_2::solve(&grid);
        }
    }
    Ok(())
}
