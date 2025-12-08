use std::{collections::BinaryHeap, fs::read_to_string, path::PathBuf, str::FromStr};

use ordered_float::OrderedFloat;

#[derive(Debug, PartialEq, Eq, Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
    z: i64
}


#[derive(PartialEq, Eq)]
struct UnionFind {
    parents: Vec<usize>,
    sizes: Vec<usize>,
    positions: Vec<Point>,
    num_groups: usize
}


impl Point {
    fn dist(&self, other: &Point) -> OrderedFloat<f32> {
        let sq_dist = (self.x - other.x).pow(2) + (self.y - other.y).pow(2) + (self.z - other.z).pow(2);
        OrderedFloat((sq_dist as f32).sqrt())
    }
}

#[derive(Debug, PartialEq, Eq)]
struct PointParseError;

impl FromStr for Point {
    type Err = PointParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let coords: Vec<i64> = s.trim().splitn(3, ',').map(|i| i.parse().unwrap()).collect();
        let [x, y, z] = coords.try_into().unwrap();
        Ok(Point {x, y, z})
    }
}

impl UnionFind {
    fn from_points(points: &[Point]) -> Self {
        let n = points.len();
        UnionFind { 
            parents: (0..n).collect(), 
            sizes: vec![1; n],
            positions: Vec::from(points),
            num_groups: n
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parents[x] != x {
            self.parents[x] = self.find(self.parents[x]);
        }

        return self.parents[x];
    }

    fn union(&mut self, x: usize, y: usize) {
        let x = self.find(x);
        let y = self.find(y);
        if x == y {
            return
        }
        self.num_groups -= 1;
        let size_x = self.sizes[x];
        let size_y = self.sizes[y];

        if size_x < size_y {
            self.parents[x] = self.parents[y];
            self.sizes[y] += self.sizes[x];
        } else {
            self.parents[y] = self.parents[x];
            self.sizes[x] += self.sizes[y];
        }
    }
}

pub fn solution2(file_path: &PathBuf) {
    let input = read_to_string(file_path).unwrap().trim().to_string();
    let n = input.lines().count();
    let points: Vec<Point> = input.lines().map(|p| p.parse().unwrap()).collect();
    
    let mut distances: BinaryHeap<(OrderedFloat<f32>, (usize, usize))> = BinaryHeap::new();
    for i in 0..n {
        for j in (i+1)..n {
            let dist = points[i].dist(&points[j]);
            distances.push((-dist, (i, j)));
        }
    }

    let mut uf = UnionFind::from_points(&points);
    let mut last_joined_x_coords: (i64, i64) = (0, 0);
    while uf.num_groups > 1 && let Some((_, (a, b))) = distances.pop() {
        uf.union(a, b);
        last_joined_x_coords = (uf.positions[a].x, uf.positions[b].x);
    }

    println!("The answer is... {}", last_joined_x_coords.0 * last_joined_x_coords.1);
}
